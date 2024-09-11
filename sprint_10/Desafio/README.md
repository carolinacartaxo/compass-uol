# Última etapa do Desafio  
## Primeiro passo: Perguntas a serem respondidas
Nessa etapa, como trabalhamos com visualização de dados, eu criei algumas querys e alguns gráficos com meus dados para analisar melhor minha base de dados. Visto que minhas perguntas anteriores são atreladas a ascpectos de popularidade, decidi fazer uma análise mais geral de aspectos de popularidade dos filmes dos gêneros trabalhados em um período de tempo.
<br />Essa mudança se deu ao fato de que a análise se tornaria mais direcionada especificamente à aspectos que possam influenciar na manutenção da popularidade de um filme dos gêneros "crime" ou "guerra" que foi lançado nos últimos 5 anos.
<br />
<br />
Minha "pergunta" ficou assim:
#### Análise de critérios relacionados à popularidade dos filmes dos gêneros "Crime" ou "Guerra" lançados entre os anos de 2018 a 2023
Novamente, decidi limitar todo o escopo da minha pesquisa ao período de 2018 a 2023 e analisar especificamente aspectos desses filmes que possam ter influenciado na popularidade deles. 

## Segundo passo: Explicação dos itens puxados para as tabelas e modelagem dimensional com a tabela fato e as tabelas dimensões
Originalmente, visando responder às minhas perguntas anteriores, eu tinha puxado os seguintes dados: movie_id, actor_name, actor_gender, actor_profession, original_title, release_year, genre, fact_movies, popularity, average_rating e vote_count.
Mantive os títulos em inglês pois as informações das tabelas também estão em inglês. 
<br /> 
<br />
Pensando nesses dados, decidi criar minha tabela fato apenas com as informações quantitativas dos filmes e criar duas tabelas dimensões, uma com as informações descritivas dos atores e outra dos filmes.
A chave primária(PK) aqui será movies_id e ela será a FK tanto da tabela fact_movies, quanto da tabela dim_movies, sendo chave estrangeira (FK) na tabela dim_actors, visto que as informações dos atores foram retiradas do csv e estão conectadas ao id imdb dos filmes, que é o movie_id aqui.

![Image](/sprint_09/Desafio/tabelas_dimensionais.png)

Mantive dessa forma no código, mas ainda puxei outro item da API do TMDB, um item que se chama "bellongs_to_collection". Esse item, está em uma estrutura aninhada no JSON e ele diz se o filme pertence a alguma "collection" que em português seria franquia. Decidi quebrar o item em duas colunas: "collection_id" e "collection_name". 
<br />
<br />
Para os filmes que não fazem parte de franquia, o JSON os retornaria com os espaços dessas colunas como "null", vazios. 
Visto que minha análise mudou, percebi que a tabela dim_actors não seria essencial à minha análise e acabei trabalhando apenas com as tabelas fact_movies e dim_movies

![Image](/sprint_10/Desafio/diagrama_relacional_atual.png)


## Terceiro passo: correções no código do Glue
<br />
Visto que puxei novos dados ao pegar "bellongs_to_collection", alterei meu código no Lambda para puxar esses novos dados e refiz o procedimento dos Jobs do Glue de puxar os dados da cada Raw para a Trusted e para a Refined.
<br /> 
Percebi que estava convertendo meus códigos para Dynamic Frame e que isso deu problema em alguns dados e não era necessário fazer essa conversão. Mudei essa parte nos meus Jobs e deixei todos os Jobs como DataFrame Spark. 
<br />
Ainda nos meus código no Glue, alterei meu código da camada refined (agora criando as novas colunas collection_id e collection_name). Realizei join das colunas e dropei os dados duplicados, pois vi que meus joins estavam duplicando os dados dos filmes por conta da quantidade de atores que se repete em cada filme.
<br />
Durante esses processos, na camada Trusted eu mantive o refinamento para o período de filmes lançados entre "2018 a 2023" e para filmes dos gêneros "crime" ou "guerra".
<br />

[Código Python representando o AWS Glue - Refined com explicações em markdown](/sprint_10/Desafio/codigo_glue_refined.py)

## Quarto passo: construção do Dashboard
Agora falando sobre o dashboard, minha hipótese ao criar o dashboard foi originalmente analisar se o número de votos ou a data de lançamento de filmes influencia na popularidade atual dos filmes.
<br />Visto que meu squad pegou os gêneros de "crime" ou "guerra", me detive à esses gêneros e fiz uma análise dos últimos 5 anos de filmes lançados.
Não posso falar de popularidade sem antes explicar a métrica de popularidade usada pelo TMDB, que é onde puxamos a pontuação de popularidade dos filmes.
<br />
<br />
O TMDB considera para a sua pontuação de popularidade dos Filmes os seguintes aspectos:
<ul>
  <li> Número de votos do dia </li>
  <li> Número de visualizações do dia</li>
  <li> Número de usuários que marcaram como "favorito" do dia </li>
  <li> Número de usuários que adicionaram à sua "lista para assistir depois" do dia </li>
  <li> Data de lançamento </li>
  <li> Número total de votos </li>
  <li> Pontuação dos dias anteriores </li>
</ul>

Estudando esses critérios e os dados, percebi que a popularidade é uma métrica difícil de ter relação com um só fator. 
Filmes mais recentes tendem a ter uma pontuação de popularidade maior visto que mais pessoas vão favoritá-lo por ser mais recente e estar mais "visível" nas mídias.
Analisando minha base de dados, percebi que, de 2018 a 2023, teve uma variação na média de popularidade total comparado ao número de filmes lançados em cada ano.
Em 2018 e especialmente em 2020, a distribuição média de popularidade, se comparada à quantidade de filmes lançados, tem uma grande queda se comparado aos outros anos analisados
Dito isso, peguei uma amostra dos 50 filmes mais populares e analisei o período que eles foram lançados. No segundo gráfico percebemos que poucos filmes do top 50 foram lançados em 2018 e em 2020, porém, a média de popularidade desses anos é bastante alta para poucos filmes, mas não há uma distorção tão grande na popularidade destes.
<br />
<br />
![Image](/sprint_10/Evidencias/02.png)
<br />
<br />
Investigando mais aspectos que poderiam influenciar na popularidade, vi que não há uma relação entre a popularidade dos filmes e a nota média destes. Para isso, analisei uma amostra a partir dos 50 filmes mais votados já para tirar os outliers que seriam os dados com poucos votos e nota alta.
<br />Ainda, a partir dos 50 filmes mais populares, analisei os gêneros acompanhantes dos gêneros de "Crime" ou "War"(Guerra) que mais se repetem e vi que filmes com elemento de Ação e Drama são mais preponderantes nos 50 filmes mais populares.
<br />
<br />
![Image](/sprint_10/Evidencias/03.png)
<br />
<br />
Passando para a última linha do meu dashboard, analisei se a popularidade teria alguma relação com minha hipótese inicial de que o número de votos poderia influenciar diretamente na popularidade dos filmes.
<br />Analisando a relação entre a popularidade dos filmes e a quantidade de votos que estes receberam, a partir de uma amostra dos 50 filmes mais votados. Vemos que não dá para dizer que tem uma forte relação pois filmes bem votados no seu lançamento não necessariamente mantiveram a sua popularidade até hoje.
<br />Ainda neste gráfico, percebi que dois filmes muito populares foram lançados nos anos de 2018 e 2020. Diferente de filmes de renome como o Batman e Coringa, eles não tiveram grande quantidade de votos e nem são filmes bem reconhecidos, mas permanecem popular.
Esses filmes são "Bad Boys for Life" e "The Equalizer 2".
<br />
<br />
![Image](/sprint_10/Evidencias/04.png)
<br />
<br />
<br />No último gráfico, realizei uma pesquisa dentro dos filmes mais votados e mais populares de quantos destes são filmes com franquia (usando aqui meus dados do bellongs_to_collection) ou não. Percebi que, entre os filmes mais votados, os filmes com franquia, apesar de serem lançados em menor quantidade, tem uma popularidade média muito superior aos filmes sem franquia.
Analisando todos esses aspectos, percebi que, tanto o filme "Bad Boys for Life" quanto "The Equalizer 2" são filmes de franquias policiais de ação. 
<br /> Esse tipo de filme tem um nicho de público que acompanha os lançamentos de novos filmes das franquias. Os filmes também contam com atores de renome, mas a manutenção da sua popularidade poderia ser atribuída mais ao estilo de filme que parece ter um público engajado em acompanhá-los, o que explicaria a popularidade alta deles mesmo que eles tenham sido lançados em anos com poucos filmes populares e mesmo não sendo filmes de conhecimento público geral como "Joker" e "Batman". 
<br />
<br />
![Image](/sprint_10/Evidencias/05.png)
<br />
<br />
## Evidências da execução do desafio no AWS Glue
![Image](/sprint_10/Evidencias/06.png)
![Image](/sprint_10/Evidencias/07.png)
![Image](/sprint_10/Evidencias/08.png)
![Image](/sprint_10/Evidencias/09.png)
![Image](/sprint_10/Evidencias/10.png)
