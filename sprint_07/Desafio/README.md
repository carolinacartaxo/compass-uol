# Explicação do Desafio 
## Primeiro passo: fazer as perguntas
### Top 10 filmes mais votados e melhor avaliados dos estados unidos, dos gêneros crime ou guerra, lançados nos últimos 4 anos (2019-2024) 
### Existe alguma relação entre a popularidade dos atores e o top 10 filmes de guerra ou crime mais populares nos últimos 4 anos ou com o top 10 da pergunta anterior? 

# Segundo passo: Dados coletados para responder as perguntas:
- TMDB:
    - Discover Movies api:
        - Por quantidade de votos: "id”; "vote_average"; "vote_count"; "popularity"; "title”; "genre_ids”; "release_date”
        - Por popularidade: "genre_ids”; "id”; "title”; "popularity”; "release_date”; "vote_average”; "vote_count”
    - Popular actors api: "id”;"popularity"; "name"; "genre_ids”; "known_for_department"; "known_for": { "id”; "genre_ids”; "popularity”};
    - Movies details: "title”, "genres”, "id”, "imdb_id”, "popularity”, "release_date”, "vote_average”, "vote_count”
- CSV: id; tituloPincipal; anoLancamento; genero; notaMedia; numeroVotos; nomeArtista; profissao; titulosMaisConhecidos;

# Terceiro passo: Explicação do Código e evidências da execução  
Primeiro eu puxei os dados dos filmes de crime ou guerra dos últimos 4 anos que tiveram maior quantidade de votos, pois se eu puxar por nota, vão vir filmes com poucas avaliações, visto que tem filmes com nota 10 que só tiveram 2 votos, por exemplo. 

Também, peguei: a api de popularidade dos filmes, dos últimos 4 anos; a api com a lista de popularidades dos atores e a api com os detalhes dos filmes. 

Para não ficar um volume de dados muito grande e, visto que a api de popularidade dos atores não tem parâmetro de limitação por data, criei um loop para limitar a quantidade de páginas para 300. Após criar esse loop, criei uma função para separar esses resultados em 100 itens por arquivo json e para mandar esses arquivos para o meu bucket no s3 em formato json. 

Por fim, para pegar os ids dos filmes na api de detalhes dos filmes, peguei os ids dos filmes da api de filmes por popularidade e criei um loop para passar esses ids na api de detalhes dos filmes. Preciso da api de detalhes dos filmes pois o código do filme no TMDB encontra-se nela.

Ao fim do código, coloquei algumas mensagens para me mostrar a quantidade de itens e páginas retornadas ao total por requisição da API. Até para, caso o código dê algum problema, ficar mais fácil entender em que ponto esse problema ocorreu.
