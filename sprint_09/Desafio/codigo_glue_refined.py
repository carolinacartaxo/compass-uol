import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, when, first

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

# Leitura dos dados da camada Trusted (em formato Parquet) como DataFrames do Spark
spark_df_local = spark.read.parquet(trusted_path_local)
spark_df_tmdb = spark.read.parquet(trusted_path_tmdb)

print("Esquema inicial do dataset Local para ver o funcionamento do código:")
spark_df_local.printSchema()

print("Esquema inicial do dataset TMDB para ver o funcionamento do código:")
spark_df_tmdb.printSchema()

# Tabela de Dimensão (dim_actors)
dim_actors_df = spark_df_local.select(
    col("id").alias("movie_id"),
    col("nomeartista").alias("actor_name"),
    col("generoartista").alias("actor_gender"),
    col("profissao").alias("actor_profession")
).dropDuplicates(["movie_id", "actor_name"])

# Tabela de Dimensão (dim_movies) com extração de belongs_to_collection para identificar se o filme faz parte de alguma franquia
dim_movies_df = spark_df_local.join(
    spark_df_tmdb,
    spark_df_local.id == spark_df_tmdb.imdb_id,
    "left"
).select(
    spark_df_local.id.alias("movie_id"),
    col("titulooriginal").alias("original_title"),
    when(col("anolancamento") == "\\N", None).otherwise(col("anolancamento").cast("int")).alias("release_year"),
    col("genero").alias("genre"),
    when(col("belongs_to_collection").isNotNull(), col("belongs_to_collection.id")).alias("collection_id"),
    when(col("belongs_to_collection").isNotNull(), col("belongs_to_collection.name")).alias("collection_name")
).dropDuplicates(["movie_id"])

# Tabela de Fato (fact_movies)
fact_movies_df = spark_df_local.join(
    spark_df_tmdb,
    spark_df_local.id == spark_df_tmdb.imdb_id
).select(
    spark_df_local.id.alias("movie_id"),
    spark_df_tmdb.popularity,
    when(col("notamedia") == "\\N", None).otherwise(col("notamedia").cast("double")).alias("average_rating"),
    when(col("numerovotos") == "\\N", None).otherwise(col("numerovotos").cast("int")).alias("vote_count")
).dropDuplicates(["movie_id"])

# Escrita dos dados na camada Refined no formato Parquet

# Tabela DimActors
dim_actors_df.write.mode("overwrite").parquet(f"{refined_path}/dim_actors/")

# Tabela DimMovies
dim_movies_df.write.mode("overwrite").parquet(f"{refined_path}/dim_movies/")

# Tabela FactMovies
fact_movies_df.write.mode("overwrite").parquet(f"{refined_path}/fact_movies/")

print(f"Dados movidos da camada Trusted para a camada Refined em: {refined_path}")

job.commit()
