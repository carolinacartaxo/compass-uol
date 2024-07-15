# Explicação do Desafio 
## Explicação do desafio, delimitação das perguntas realizadas para este e motivação destas
O desafio final trata da construção de um Data Lake com as etapas de Ingestão, Armazenamento, Processamento e Consumo com as bases de dados "movies.csv" e "series.csv" e com base em dados de API do TMDB. 
Nessa etapa inicial é importante a realização de duas perguntas para criação da análise dos dados posteriormente.
Cada squad pegou um gênero de filme/série. Meu squad ficou com o tema "Crimes" ou "Guerra" e, considerando a delimitação do tema, e os dados disponíveis, realizei as seguintes perguntas:
### 1. Top 10 atrizes dos filmes do gênero "crime" ou "guerra" melhor avaliados entre os anos 1990 e 2024;
### 2. Média de idade dos atores que participaram de filmes de guerra ou crime com as maiores notas
Criei as perguntas visando analizar quais as 10 atrizes que fizeram os filmes de crime/guerra melhor avaliados dos últimos anos e qual a média da idade dos atores que participaram desses filmes.
As perguntas serão respondidas nas próximas etapas do Desafio.

## Explicação da primeira etapa do desafio 
Essa etapa do desafio consistiu em construir um código Python, que será executado dentro de um container Docker para carregar os dados locais dos arquivos csv "movies" e "series" disponibilizados um bucket no S3 da AWS.

O código deve: 
• ler os 2 arquivos (filmes e series) no formato CSV inteiros, ou seja, sem filtrar os dados.
• utilizar a lib boto3 para carregar os dados para a AWS.
• acessar a AWS e grava no S3, no bucket definido com RAW Zone.
Devo criar o container Docker com um volume para armazenar os arquivos CSV e executar processo Python implementado e
executar localmente o container docker para realizar a carga dos dados ao S3.

1. Criei um código Python condizente com a documentação do boto3 para pegar meus dois arquivos csv e realizar o upload no S3
```
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
```


2. Após isso, fiz a criação do script dockerfile para executar o código Python em um container
3. Criei um arquivo em texto para o docker pegar e instalar as dependências necessárias, que nesse caso é a biblioteca do boto3


```# Usar uma imagem oficial do Python como base
FROM python:3.9-slim

# Definir o diretório de trabalho no container
WORKDIR /usr/src/app

# Copiar o arquivo boto3.txt para o container
COPY boto3.txt ./

# Instalar as dependências necessárias
RUN pip install --no-cache-dir -r boto3.txt

# Copiar o código da aplicação para o container
COPY . .

# Comando para executar o script Python
CMD [ "python", "./upload_to_s3.py" ]
```


4. No terminal, eu digitei `docker build -t upload-to-s3 .` para criar a imagem.
![Image](/sprint_06/Evidencias/01.png)

6. Em seguida, para conseguir encaminhar minhas credenciais da AWS para o boto3 mandar meus arquivos para o S3, eu coloquei no terminal `docker run -e AWS_ACCESS_KEY_ID="" -e AWS_SECRET_ACCESS_KEY="" -e AWS_SESSION_TOKEN="" upload-to-s3` e preenchi os espaços com minhas credenciais AWS.

![Image](/sprint_06/Evidencias/03.png)

8. Rodei o código e os arquivos foram carregados no meu bucket no formado requerido no desafio, conforme a seguinte url: s3://data-lake-ana-carolina/Raw/Local/CSV/Series/2024/07/15/series.csv
![Image](/sprint_06/Evidencias/05.png)
![Image](/sprint_06/Evidencias/06.png)
