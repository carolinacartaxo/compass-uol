# Explicação do Desafio 
## Primeiro passo: Perguntas a serem respondidas
1. Top 10 filmes mais votados e melhor avaliados dos gêneros crime ou guerra lançados entre 2018 a 2023 
2. Proporção de atores e atrizes que atuaram no top 10 filmes dos gêneros crime ou guerra mais populares lançados entre 2018 a 2023

## Segundo passo: Explicação dos itens puxados para as tabelas e modelagem dimensional com a tabela fato e as tabelas dimensões
 Para responder minhas perguntas e para facilitar a visualização, eu puxei os seguintes dados: movie_id, actor_name, actor_gender, actor_profession, original_title, release_year, genre, fact_movies, popularity, average_rating e vote_count.
Mantive os títulos em inglês pois as informações das tabelas também estão em inglês. 
Pensando nesses dados, decidi criar minha tabela fato apenas com as informações quantitativas dos filmes e criar duas tabelas dimensões, uma com as informações descritivas dos atores e outra dos filmes.
A chave primária(PK) aqui será movies_id e ela será a PK tanto da tabela fact_movies, quanto da tabela dim_movies, sendo chave estrangeira (FK) na tabela dim_actors, visto que as informações dos atores foram retiradas do csv e estão conectadas ao id imdb dos filmes, que é o movie_id aqui.

![Image](/sprint_09/Desafio/tabelas_dimensionais.png)

## Terceiro passo: explicação do código e evidências da execução
Após decidir minhas tabelas, criei um Job no Glue com as especificações pedidas no desafio e lá criei um código que lê dados do CSV e do TMDB da camada Trusted no S3, os transforma em tabelas de fato e dimensões, e salva o resultado transformado de volta no S3 em uma nova camada, chamada "Refined". 
Para criar as tabelas, eu primeiro converti de DynamicFrame para DataFrame para usar as funções do spark. Depois, usando a lógica explicada anteriormente, criei minhas tabelas dimensões e fato. Na minha tabela fato eu fiz o join da tabela local pelo movie_id com a tabela popularity do TMDB. Na criação das tabelas eu também fiz um filtro para não pegar os dados nulos que estavam como "\\N" no CSV. 
Por fim, fiz a conversão de Dataframe para DynamicFrame e os mandei para a zona Refined criada no job. 


[Código Python representando o AWS Glue - Refined com explicações em markdown](/sprint_09/Desafio/codigo_glue_refined.py)



## Evidências da execução do desafio no AWS Glue
![Image](/sprint_09/Evidencias/01.png)
![Image](/sprint_09/Evidencias/02.png)
![Image](/sprint_09/Evidencias/03.png)
![Image](/sprint_09/Evidencias/04.png)
![Image](/sprint_09/Evidencias/05.png)
![Image](/sprint_09/Evidencias/06.png)
![Image](/sprint_09/Evidencias/07.png)

