# Explicação do Desafio 
## Primeiro passo: fazer as perguntas
1. Top 10 filmes mais votados e melhor avaliados dos estados unidos, dos gêneros crime ou guerra, lançados nos últimos 4 anos (2019-2024) 
2. Existe alguma relação entre a popularidade dos atores e o top 10 filmes de guerra ou crime mais populares nos últimos 4 anos? E com o top 10 da pergunta anterior? 

## Segundo passo: Explicação dos motivadores de cada API
Primeiro eu puxei os dados dos filmes de crime ou guerra dos últimos 4 anos que tiveram maior quantidade de votos, pois se eu puxar por nota, virão filmes com poucas avaliações, visto que tem filmes com nota 10 que só tiveram 2 votos, por exemplo. Então para pegar os filmes melhor votados, eu tenho que pegar da amostra dos filmes mais votados também

Também, peguei: a api de popularidade dos filmes, dos últimos 4 anos; a api com a lista de popularidades dos atores e a api com os detalhes dos filmes. 

A api de popularidade dos filmes eu puxei para ver se tem relação a popularidade dos filmes com a popularidade dos atores. A popularidade dos filmes está filtrada para os últimos 4 anos, mas a dos atores não tem filtro de data, então abrangi a pergunta para ver se a popularidade dos atores tem relação com a popularidade dos filmes ou com a avaliação dos filmes.

Puxei essa quantidade de dados para facilitar a filtragem dos dados para a análise e também para conseguir fazer a associação deles com o CSV. Outro detalhe é que, puxei alguns dados repitidos com os dados presentes no CSV, porque o CSV tem alguns dados destoantes da API do TMDB e os dados do CSV parecem ir apenas até 2022, então puxei esses dados pela api pois parecem mais certos. 
Exemplo do filme "Knives Out" que tem notas e quantidade de votos levemente diferentes na API e no CSV
![Image](/sprint_07/Evidencias/08.png)

## Terceiro passo: explicação do código e evidências da execução

[Código Python representando o Lambda com explicações em markdown](/sprint_07/Desafio/desafio.py)

Para não ficar um volume de dados muito grande e, visto que a api de popularidade dos atores não tem parâmetro de limitação por data, criei um loop para limitar a quantidade de páginas para 300. Após criar esse loop, criei uma função para separar esses resultados em 100 itens por arquivo json e para mandar esses arquivos para o meu bucket no s3 em formato json. 

Por fim, para pegar os ids dos filmes na api de detalhes dos filmes, peguei os ids dos filmes da api de filmes por popularidade e criei um loop para passar esses ids na api de detalhes dos filmes. Preciso da api de detalhes dos filmes pois o código do filme no TMDB encontra-se nela.

Ao fim do código, coloquei algumas mensagens para me mostrar a quantidade de itens e páginas retornadas ao total por requisição da API. Até para, caso o código dê algum problema, ficar mais fácil entender em que ponto esse problema ocorreu.

- Os arquivos JSON tem 100 registros cada
- Limitei para a URL puxar até 300 páginas de dados
- Nenhum arquivo JSON chegou a 10 mb
- Os dados trazidos repetiram alguns dados fornecidos pelo CSV porque, como eu disse, o CSV só vai até 2022 e tem dados diferentes da API nos quesitos que eu preciso analisar para responder às perguntas
- Adicionei uma Layer ao Lambda para rodar as bibliotecas e aumentei um pouco o tempo de execução do CloudWatch para puxar os dados da API.  

### Evidências da execução do código no Lamdba 

![Image](/sprint_07/Evidencias/01.png)
![Image](/sprint_07/Evidencias/02.png)
![Image](/sprint_07/Evidencias/03.png)
![Image](/sprint_07/Evidencias/04.png)
![Image](/sprint_07/Evidencias/05.png)
![Image](/sprint_07/Evidencias/06.png)
![Image](/sprint_07/Evidencias/07.png)
