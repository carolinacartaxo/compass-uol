import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import lit, col, when

## @params: [JOB_NAME, S3_TRUSTED_PATH_LOCAL, S3_TRUSTED_PATH_TMDB, S3_REFINED_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_TRUSTED_PATH_LOCAL', 'S3_TRUSTED_PATH_TMDB', 'S3_REFINED_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos de origem e destino
trusted_path_local = args['S3_TRUSTED_PATH_LOCAL']
trusted_path_tmdb = args['S3_TRUSTED_PATH_TMDB']
refined_path = args['S3_REFINED_PATH']

# Leitura dos dados da camada Trusted 
df_local = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [trusted_path_local]},
    format="parquet"
)

df_tmdb = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [trusted_path_tmdb]},
    format="parquet"
)

# Esquemas para ver como estão os dados e o funcionamento do código
print("Esquema inicial do dataset Local para ver o funcionamento do código:")
df_local.printSchema()

print("Esquema inicial do dataset TMDB para ver o funcionamento do código:")
df_tmdb.printSchema()

# Convertendo DynamicFrames para DataFrames do Spark para fazer a modelagem com as funções do spark
spark_df_local = df_local.toDF()
spark_df_tmdb = df_tmdb.toDF()

# Transformações para criar as tabelas Fato e Dimensões

# Tabela de Dimensão Atores (dim_actors)
dim_actors_df = spark_df_local.select(
    col("id").alias("movie_id"),
    col("nomeartista").alias("actor_name"),
    col("generoartista").alias("actor_gender"),
    col("profissao").alias("actor_profession")
)

# Tabela de Dimensão Filmes (dim_movies)
dim_movies_df = spark_df_local.select(
    col("id").alias("movie_id"),
    col("titulooriginal").alias("original_title"),
    when(col("anolancamento") == "\\N", None).otherwise(col("anolancamento").cast("int")).alias("release_year"),
    col("genero").alias("genre")
)

# Tabela de Fato Filmes (fact_movies)
fact_movies_df = spark_df_local.join(spark_df_tmdb, spark_df_local.id == spark_df_tmdb.imdb_id).select(
    spark_df_local.id.alias("movie_id"),
    spark_df_tmdb.popularity,
    when(col("notamedia") == "\\N", None).otherwise(col("notamedia").cast("double")).alias("average_rating"),
    when(col("numerovotos") == "\\N", None).otherwise(col("numerovotos").cast("int")).alias("vote_count")
)

# Convertendo DataFrames do Spark de volta para DynamicFrames da AWS para levar os dados ao bucket 
dynamic_frame_dim_actors = DynamicFrame.fromDF(dim_actors_df, glueContext, "dynamic_frame_dim_actors")
dynamic_frame_dim_movies = DynamicFrame.fromDF(dim_movies_df, glueContext, "dynamic_frame_dim_movies")
dynamic_frame_fact_movies = DynamicFrame.fromDF(fact_movies_df, glueContext, "dynamic_frame_fact_movies")

# Escrevendo os dados na camada Refined no formato Parquet

# Tabela DimActors
glueContext.write_dynamic_frame.from_options(
    frame=dynamic_frame_dim_actors,
    connection_type="s3",
    connection_options={
        "path": f"{refined_path}/dim_actors/"
    },
    format="parquet"
)

# Tabela DimMovies
glueContext.write_dynamic_frame.from_options(
    frame=dynamic_frame_dim_movies,
    connection_type="s3",
    connection_options={
        "path": f"{refined_path}/dim_movies/"
    },
    format="parquet"
)

# Tabela FactMovies
glueContext.write_dynamic_frame.from_options(
    frame=dynamic_frame_fact_movies,
    connection_type="s3",
    connection_options={
        "path": f"{refined_path}/fact_movies/"
    },
    format="parquet"
)

# Print final só para visualizar no CloudWatch se o código foi bem sucedido
print(f"Dados movidos da camada Trusted para a camada Refined em: {refined_path}")

job.commit()