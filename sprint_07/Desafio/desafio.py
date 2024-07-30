import requests
import json
import boto3
import os
from datetime import datetime

# Configurar as URLs da API do TMDB
urls = {
    "quantidade_votos": "https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&language=en-US&page={page}&primary_release_date.gte=2019-01-01&release_date.lte=2024-01-01&sort_by=vote_count.desc&with_genres=80%20%7C%2010752&with_origin_country=US&with_original_language=en",
    "popularidade_atores": "https://api.themoviedb.org/3/person/popular?language=en-US&page={page}",
    "popularidade_filmes": "https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&language=en-US&page={page}&primary_release_date.gte=2019-01-01&release_date.lte=2024-01-01&sort_by=popularity.desc&with_genres=80%20%7C%2010752&with_origin_country=US&with_original_language=en"
}

# Cabeçalhos da requisição
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {os.getenv('API_KEY')}"
}

# Cliente S3
s3 = boto3.client('s3')
bucket_name = os.getenv('BUCKET_NAME')
storage_layer = 'Raw'
data_origin = 'TMDB'
data_format = 'JSON'
date_path = datetime.now().strftime('%Y/%m/%d')

# Função para obter dados da API
def obter_dados(url_template, campos_desejados):
    dados = []
    page = 1

    # Loop para coletar dados até atingir 300 páginas ou não haver mais resultados
    while page <= 300:
        url = url_template.format(page=page) # Formata a URL com o número da página atual
        response = requests.get(url, headers=headers) # Faz a requisição para a API
        response.raise_for_status() # Levanta uma exceção se a requisição falhar
        data = response.json() # Converte a resposta em um objeto JSON
        if 'results' in data:
            for item in data['results']:
                item_filtrado = {campo: item[campo] for campo in campos_desejados if campo in item}
                dados.append(item_filtrado)
            if len(data['results']) == 0:
                break # Sai do loop se a página atual não contiver resultados
        else:
            break  # Sai do loop se não houver mais resultados
        page += 1
    return dados

# Função para salvar e enviar os dados em partes (arquivos JSON com até 100 registros cada)
def salvar_e_enviar_json(dados, prefixo):
    try:
        for i in range(0, len(dados), 100):
            parte_dados = dados[i:i + 100] # Divide os dados em partes de 100
            json_file = json.dumps(parte_dados, ensure_ascii=False, indent=4) # Salva a parte atual em um arquivo JSON
            file_name = f'{prefixo}_parte_{i // 100 + 1}.json' # Cria o nome do arquivo
            s3_key = f"{storage_layer}/{data_origin}/{data_format}/{date_path}/{file_name}" # Cria o caminho do arquivo no bucker
            s3.put_object(Bucket=bucket_name, Key=s3_key, Body=json_file.encode('utf-8')) # Envia o arquivo para o bucket
            print(f'Enviado {file_name} para o S3 com sucesso')
    except Exception as e:
        print(f"Erro ao enviar {file_name} para o S3: {str(e)}")
        raise

# Função para obter detalhes de filmes usando seus IDs
def obter_detalhes_filmes(ids_filmes):
    detalhes_filmes = []
    for filme_id in ids_filmes:
        url = f"https://api.themoviedb.org/3/movie/{filme_id}?language=en-US" # Inserindo os ids dos fimes para pegar dados da API
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        item_filtrado = { # Filtrando os dados da requisição
            "title": data.get("title"),
            "genres": data.get("genres"),
            "id": data.get("id"),
            "imdb_id": data.get("imdb_id"),
            "origin_country": data.get("production_countries"),
            "popularity": data.get("popularity"),
            "release_date": data.get("release_date"),
            "vote_average": data.get("vote_average"),
            "vote_count": data.get("vote_count")
        }
        detalhes_filmes.append(item_filtrado)
    salvar_e_enviar_json(detalhes_filmes, 'detalhes_filmes')
    return len(detalhes_filmes)

def lambda_handler(event, context):
    try:
        print("Iniciando coleta de dados")
        
        # Coletar dados das três URLs principais
        campos_filmes = ["genre_ids", "id", "title", "popularity", "release_date", "vote_average", "vote_count"]
        campos_atores = ["id", "name", "popularity", "known_for", "gender"]
        
        # Retornar informações dos dados e me informar os pontos de funcionamento da requisição
        filmes_quantidade_votos = obter_dados(urls["quantidade_votos"], campos_filmes)
        print(f"Filmes por quantidade de votos coletados: {len(filmes_quantidade_votos)}")
        salvar_e_enviar_json(filmes_quantidade_votos, 'filmes_quantidade_votos')
        
        atores_popularidade = obter_dados(urls["popularidade_atores"], campos_atores)
        print(f"Atores populares coletados: {len(atores_popularidade)}")
        salvar_e_enviar_json(atores_popularidade, 'atores_popularidade')
        
        filmes_popularidade = obter_dados(urls["popularidade_filmes"], campos_filmes)
        print(f"Filmes populares coletados: {len(filmes_popularidade)}")
        salvar_e_enviar_json(filmes_popularidade, 'filmes_popularidade')

        # Obter IDs dos filmes populares
        ids_filmes_populares = [filme['id'] for filme in filmes_popularidade]

        # Obter detalhes dos filmes populares
        detalhes_filmes_count = obter_detalhes_filmes(ids_filmes_populares)

        print("Processo concluído com sucesso")
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Dados processados e enviados para o S3 com sucesso."
            })
        }
    except Exception as e:
        print(f"Erro: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Erro ao processar os dados.",
                "error": str(e)
            })
        }