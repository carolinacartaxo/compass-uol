import requests
import json
import boto3
import os
from datetime import datetime

# Configurar as URLs da API do TMDB
urls = {
    "popularidade_filmes": "https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&language=en-US&page={page}&primary_release_date.gte=2018-01-01&release_date.lte=2023-01-01&sort_by=popularity.desc&with_genres=80%20%7C%2010752&with_origin_country=US&with_original_language=en"
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

def obter_dados(url_template, campos_desejados):
    """
    Função para obter dados da API do TMDB.

    Args:
    - url_template: URL com o template para a requisição.
    - campos_desejados: Campos que queremos extrair dos dados.

    Retorna:
    - Lista de dados obtidos da API.
    """
    dados = []
    page = 1

    # Loop para percorrer todas as páginas disponíveis na API
    while True:
        url = url_template.format(page=page)
        response = requests.get(url, headers=headers)
        
        # Verifica se a página é inválida
        if response.status_code == 400:
            print(f"Página {page} inválida para a URL {url}")
            break
        
        # Levanta uma exceção se a requisição falhar
        response.raise_for_status()
        
        # Converte a resposta em JSON
        data = response.json()
        
        # Verifica se há resultados na resposta
        if 'results' in data:
            for item in data['results']:
                # Filtra os campos desejados
                item_filtrado = {campo: item[campo] for campo in campos_desejados if campo in item}
                dados.append(item_filtrado)
            
            # Sai do loop se não houver mais resultados
            if len(data['results']) == 0:
                break
        else:
            break
        
        # Incrementa a página para a próxima iteração
        page += 1
    
    return dados

def salvar_e_enviar_json(dados, prefixo):
    """
    Função para salvar dados em JSON e enviar para o S3.

    Args:
    - dados: Lista de dados para salvar e enviar.
    - prefixo: Prefixo do nome do arquivo.

    Envia os arquivos JSON para o S3.
    """
    try:
        # Divide os dados em partes de 100 e salva cada parte
        for i in range(0, len(dados), 100):
            parte_dados = dados[i:i + 100]
            json_file = json.dumps(parte_dados, ensure_ascii=False, indent=4)
            file_name = f'{prefixo}_parte_{i // 100 + 1}.json'
            s3_key = f"{storage_layer}/{data_origin}/{data_format}/{date_path}/{file_name}"
            s3.put_object(Bucket=bucket_name, Key=s3_key, Body=json_file.encode('utf-8'))
            print(f'Enviado {file_name} para o S3 com sucesso')
    except Exception as e:
        print(f"Erro ao enviar {file_name} para o S3: {str(e)}")
        raise

def obter_detalhes_filmes(ids_filmes):
    """
    Função para obter detalhes de filmes usando seus IDs.

    Args:
    - ids_filmes: Lista de IDs dos filmes.

    Retorna:
    - Número de detalhes de filmes obtidos.
    """
    detalhes_filmes = []
    for filme_id in ids_filmes:
        url = f"https://api.themoviedb.org/3/movie/{filme_id}?language=en-US"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        # Filtra os campos desejados
        item_filtrado = {
            "id": data.get("id"),
            "imdb_id": data.get("imdb_id")
        }
        detalhes_filmes.append(item_filtrado)
    
    salvar_e_enviar_json(detalhes_filmes, 'detalhes_filmes')
    return len(detalhes_filmes)

def lambda_handler(event, context):
    """
    Função principal para ser executada como Lambda Handler.

    Args:
    - event: Evento que acionou a função.
    - context: Contexto da execução da função.

    Retorna:
    - Resposta indicando sucesso ou falha.
    """
    try:
        print("Iniciando coleta de dados")
        
        # Coletar dados da URL de popularidade dos filmes
        campos_filmes = ["id", "popularity"]
        
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

