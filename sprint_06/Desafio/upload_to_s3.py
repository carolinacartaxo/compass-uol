import boto3
from datetime import datetime

# Cria o cliente S3
s3 = boto3.client('s3')

# Define o nome do bucket e os caminhos dos arquivos
bucket_name = 'data-lake-ana-carolina'
movies_file = 'movies.csv'
series_file = 'series.csv'

# Data atual para o padrão de armazenamento
today = datetime.now()
date_path = today.strftime('%Y/%m/%d')

# Faz o upload dos arquivos
s3.upload_file(movies_file, bucket_name, f'Raw/Local/CSV/Movies/{date_path}/movies.csv')
s3.upload_file(series_file, bucket_name, f'Raw/Local/CSV/Series/{date_path}/series.csv')

print("Arquivos carregados com sucesso!")
