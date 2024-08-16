import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import lit

## @params: [JOB_NAME, S3_INPUT_PATH, S3_TARGET_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminho de entrada e saída no S3
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# Extrair a data de coleta do caminho S3
s3_path_parts = source_file.split('/')
data_coleta = f"{s3_path_parts[-4]}-{s3_path_parts[-3]}-{s3_path_parts[-2]}"

# Leitura dos dados JSON do TMDB da Raw Zone
df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [source_file]
    },
    "json",
    {"multiline": False}
)

# Verificação do esquema inicial
print("Esquema inicial:")
df.printSchema()

# Adicionando a coluna 'dt' com a data de coleta formatada como 'yyyy-MM-dd'
spark_df = df.toDF()
spark_df = spark_df.withColumn("dt", lit(data_coleta))

# Verificação do esquema e amostra dos dados
print("Esquema após adicionar a coluna de data:")
spark_df.printSchema()
spark_df.show(5)

# Convertendo de volta para DynamicFrame
dynamic_frame = DynamicFrame.fromDF(spark_df, glueContext, "dynamic_frame")

# Escrita dos dados particionados no S3 em formato Parquet
glueContext.write_dynamic_frame.from_options(
    frame=dynamic_frame,
    connection_type="s3",
    connection_options={
        "path": target_path,
        "partitionKeys": ["dt"]  # Particionando por data de coleta
    },
    format="parquet"
)

job.commit()

