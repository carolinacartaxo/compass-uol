import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME, S3_INPUT_PATH, S3_TARGET_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']


df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [source_file]
    },
    "csv",
    {"withHeader": True, "separator": "|"}
)

print("Esquema inicial:")
df.printSchema()

print("Amostra dos dados:")
df.show(20) 

# Filtragem dos dados para os gêneros 'Crime' ou 'War', lançados entre 2018 e 2023
filtered_df = df.filter(lambda row: 
                        'Crime' in row['genero'] or 'War' in row['genero'] and 
                        2018 <= int(row['anoLancamento']) <= 2023)


print("Esquema após a filtragem:")
filtered_df.printSchema()
print("Número de registros após a filtragem:", filtered_df.count())

# Se houver registros, escreva o resultado na camada Trusted em formato Parquet
if filtered_df.count() > 0:
    glueContext.write_dynamic_frame.from_options(
        frame=filtered_df,
        connection_type="s3",
        connection_options={"path": target_path},
        format="parquet"
    )
    print(f"Dados filtrados foram gravados em {target_path}")
else:
    print("Nenhum registro encontrado após a filtragem. Pastas no S3 não foram criadas.")

job.commit()

