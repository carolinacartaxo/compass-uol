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

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

#Particionando os dados por data
s3_path_parts = source_file.split('/')
data_coleta = f"{s3_path_parts[-4]}-{s3_path_parts[-3]}-{s3_path_parts[-2]}"

df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [source_file]
    },
    "json",
    {"multiline": False}
)

# Me mostra os dados iniciais para eu ver o funcionamento do código
print("Esquema inicial:")
df.printSchema()

spark_df = df.toDF()
spark_df = spark_df.withColumn("dt", lit(data_coleta))

print("Esquema após adicionar a coluna de data:")
spark_df.printSchema()
spark_df.show(5)

# Convertendo de volta para DynamicFrame
dynamic_frame = DynamicFrame.fromDF(spark_df, glueContext, "dynamic_frame")

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

