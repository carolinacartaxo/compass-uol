# Explicação do Desafio 
## Primeiro passo: Perguntas a serem respondidas
1. Top 10 filmes mais votados e melhor avaliados dos gêneros crime ou guerra lançados entre 2018 a 2023 
2. Proporção de atores e atrizes que atuaram no top 10 filmes dos gêneros crime ou guerra mais populares lançados entre 2018 a 2023

## Segundo passo: Explicação dos motivadores de cada API
O CSV possui os dados dos filmes puxados da plataforma do IMDB. Considerando isso, posso responder a primeira pergunta só com os dados retirados dele através dos dados "notaMedia", "numeroVotos", "genero" e "anoLancamento".
Já para a segunda pergunta, preciso saber a popularidade dos filmes dos gêneros crime ou guerra mais populares lançados entre 2018 a 2023 e esse dado não tem no CSV. Para pegar esse dado puxei dois tipos de APIs do TMDB: a API de popularidade dos filmes dos gêneros crime ou guerra lançados entre 2018 a 2023; e a API de detalhes dos filmes, visto que na parte de detalhes tenho o código do IMDB dos filmes.

O CSV não tem dados de popularidades dos filmes, mas a API de popularidade dos filmes nos possibilita puxar a pontuação de popularidade destes, permitindo que filtremos esses filmes por gêneros e ano de lançamento. Dessa API eu peguei apenas o "id" e a "popularity", que corresponde à pontuação de popularidade do filme, e filtrei por filmes dos gêneros "guerra" ou crime" lançados entre 2018 a 2023.
Esse filtro já nos permite pegar os 10 filmes mais populares com os requisitos da pergunta e, a partir disso, pegar as atrizes e os atores que estrelaram nestes para que possamos tirar a proporção final .

![Image](/sprint_07/Evidencias/08.png)

## Terceiro passo: explicação do código e evidências da execução
Partindo para o terceiro passo, na sprint passada eu puxei os dados necessários da API do TMDB (pontuação de popularidade e código do IMDB) para a camada Raw, bem como, todos os dados do CSV para esta mesma camada, com a única diferença de que, estes estão em uma pasta local e os dados da API do TMDB estão na pasta do TMDB e separados por data de coleta.
Considerando isso, nessa sprint eu puxei esses dados da camada Raw para a camada Trusted através do AWS Glue. No Glue, eu fiz uma filtragem dos dados do CSV para selecionar apenas aqueles relevantes para a análise, ou seja, aqueles do gênero "War" ou "Crime" e com filmes cuja data de lançamento esteve entre 2018 a 2023.
Já os dados do TMDB, como já estavam filtrados, apenas realizei a puxada dele e o seu particionamento por data, conforme pediu o desafio 

[Código Python representando o AWS Glue - CSV com explicações em markdown](/sprint_08/Desafio/codigo_glue_csv)

[Código Python representando o AWS Glue - TMDB com explicações em markdown](/sprint_08/Desafio/codigo_glue_TMDB)


## Evidências da execução do desafio no AWS Glue
![Image](/sprint_08/Evidencias/01.png)
![Image](/sprint_08/Evidencias/02.png)
![Image](/sprint_08/Evidencias/03.png)
![Image](/sprint_08/Evidencias/04.png)
![Image](/sprint_08/Evidencias/05.png)
![Image](/sprint_08/Evidencias/06.png)
![Image](/sprint_08/Evidencias/07.png)
![Image](/sprint_08/Evidencias/08.png)
![Image](/sprint_08/Evidencias/09.png)
![Image](/sprint_08/Evidencias/10.png)
![Image](/sprint_08/Evidencias/11.png)
![Image](/sprint_08/Evidencias/12.png)
![Image](/sprint_08/Evidencias/13.png)
![Image](/sprint_08/Evidencias/14.png)
![Image](/sprint_08/Evidencias/15.png)
![Image](/sprint_08/Evidencias/16.png)

