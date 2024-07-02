import boto3

# Configurar o cliente S3 utilizando as credenciais configuradas na AWS CLI
s3_client = boto3.client('s3')

# Nome do bucket e chave do objeto
bucket_name = 'prounibolsas'
object_key = 'prouni_relatorio_bolsas_2020.csv'

# Ler a consulta SQL do arquivo .sql
with open('query.sql', 'r') as file:
    expression = file.read()

# Executar a consulta S3 Select
response = s3_client.select_object_content(
    Bucket=bucket_name,
    Key=object_key,
    ExpressionType='SQL',
    Expression=expression,
    InputSerialization={'CSV': {'FileHeaderInfo': 'USE'}},  # Certificar que a primeira linha é tratada como cabeçalho
    OutputSerialization={'CSV': {}}
)

# Inicializar uma string para armazenar os dados CSV
result_data = ""
for event in response['Payload']:
    if 'Records' in event:
        result_data += event['Records']['Payload'].decode('utf-8')
    elif 'Stats' in event:
        print("Processed: ", event['Stats']['Details']['BytesProcessed'], " bytes")

if result_data:
    print("Results:\n", result_data)
else:
    print("No results found or there was an error in the query.")


