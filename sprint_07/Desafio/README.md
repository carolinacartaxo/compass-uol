# Explicação do Desafio 
## Primeiro passo: Perguntas a serem respondidas
1. Top 10 filmes mais votados e melhor avaliados dos gêneros crime ou guerra lançados entre 2018 a 2023 
2. Proporção de atores e atrizes que atuaram no top 10 filmes dos gêneros crime ou guerra mais populares lançados entre 2018 a 2023

## Segundo passo: Explicação dos motivadores de cada API
O CSV contém os seguinte dados: 
- id; tituloPincipal; anoLancamento; genero; notaMedia; numeroVotos; nomeArtista; profissao; titulosMaisConhecidos;
  
Considerando esses dados, posso responder a primeira pergunta só com os dados retirados dele através dos dados "notaMedia", "numeroVotos", "genero" e "anoLancamento"
Já para a segunda pergunta, preciso saber a popularidade dos filmes e esse dado não tem no CSV. Para pegar esse dado puxei dois tipos de APIs do TMDB. A API de popularidade dos filmes e a API de detalhes dos filmes.

O CSV não tem dados de popularidades dos filmes, mas a API de popularidade dos filmes nos possibilita puxar a pontuação de popularidade dos filmes, permitindo que filtremos esses filmes por gêneros e ano de lançamento. Dessa API eu peguei apenas o "id" e a "popularity", que corresponde à pontuação de popularidade, e filtrei por filmes dos gêneros "guerra" ou crime" lançados entre 2018 a 2023.

Esse filtro já nos permite pegar os 10 filmes mais populares com os requisitos da pergunta. Para pegar o título dos filmes, visto que o desafio pede para ser dados complementares ao CSV e nos pede para não repetir os dados nele presentes, eu peguei os dados da API "details" dos filmes, visto que é nela que temos o id do filme e o ID do TMDB. Assim, posso pegar o ID do filme popular e pegar seu ID do TMDB. Esse ID do TMDB serve para pegar informações no CSV, visto que os ids dos filmes do CSV estão nesse formato do TMDB 

![Image](/sprint_07/Evidencias/07.png)
![Image](/sprint_07/Evidencias/08.png)

## Terceiro passo: explicação do código e evidências da execução

[Código Python representando o Lambda com explicações em markdown](/sprint_07/Desafio/codigo_lambda.py)

Devido as limitações de itens por arquivos JSON pedidas no desafio, criei uma função para separar os resultados das API em 100 itens por arquivo json e para mandar esses arquivos para o meu bucket no s3 com o "path" no formato requisitado dentro da pasta RAW. 

Por fim, para pegar os ids dos filmes na api de detalhes dos filmes, peguei os ids dos filmes da api de filmes por popularidade e criei um loop para passar esses ids na api de detalhes dos filmes. 

Ao fim do código, coloquei algumas mensagens para me mostrar a quantidade de itens e páginas retornadas ao total por requisição da API. Até para, caso o código dê algum problema, ficar mais fácil entender em que ponto esse problema ocorreu.

- Os arquivos JSON tem 100 registros cada
- Nenhum arquivo JSON chegou a 10 mb
- Os dados trazidos são complementares aos dados do CSV e não repetem nenhum dado presente no CSV
- Adicionei uma Layer ao Lambda para rodar as bibliotecas e aumentei um pouco o tempo de execução do CloudWatch para puxar os dados da API.  

### Evidências da execução do código no Lamdba 

![Image](/sprint_07/Evidencias/01.png)
![Image](/sprint_07/Evidencias/02.png)
![Image](/sprint_07/Evidencias/03.png)
![Image](/sprint_07/Evidencias/04.png)
![Image](/sprint_07/Evidencias/05.png)
![Image](/sprint_07/Evidencias/06.png)

