Pasta com os entregáveis da Sprint 03, quais sejam: os exercícios requeridos com a base de dados actors.csv e o notebook referente às análises feitas com uso das bibliotecas Pandas e Matplotlib na base de dados googleplaystore.csv


# Desafio

[Resolução e explicação do Desafio](/sprint_03/Desafio/desafio.ipynb)

# Exercícios


1. [Resposta Ex1. - Com a explicação em markdown no código](/sprint_03/Exercicio/actors.py)

Passoa a passo da explicação do código em questão:
1. No exercício em questão eu comecei abrindo o arquivo CSV com o 'with open'
2. Após isso, criei a variável para receber conteúdo do arquivo, e chamei splitlines para separar as linhas
3. Depois, criei uma lista 'coluna' para receber os nomes dos cabeçalhos, estes serão usados para criar as chaves dos dicionários, como se vê a partir do 'for line in reader'
4. A partir da linha[1], vamos os valores da tabela. Cada linha do arquivo será combinado com o cabeçalho para criar um dicionário
5. Caso algum dos valores possua vírgula que não signifique divisão entre tabelas, devemos encontrar o valor problemático e assegurar que ele apareça em uma única coluna
6. Depois, vamos vasculhar cada caractere da linha problemática em busca de " " pois estes simbolizam que tudo pertence a uma coluna, apesar da vírgula
7. Caso algum caractere seja encontrado, salvaremos a posição [integer] dele na lista n
8. Caso n seja igual a 2, encontramos a palavra, devemos:
   </br> 8.1. colocar a palavra encontrada em substring,
   </br>8.2. Separar o resto da linha em lista por vírgula
   </br>8.3. Concatenar a palavra e a lista em um único dicionário
9. Cada coluna é acrescentada ao dicionário vazio "Value" por meio da variável insert
10. Ao final do loop da linha, devemos adicionar o dicionário "Value" na lista dataset para montar a nossa base de dados
 </br>
 </br>
3.1 Etapa 1: Nome do ator/atriz com maior número de filmes e respectiva quantidade
 </br>1. A cada linha comparamos o valor do número de filmes com o valor do contador, caso seja superior, atualizamos o contador e salvamos o nome do ator. Depois basta imprimir as duas variáveis
 </br>
 </br>
3.2 Etapa 2: Média de bilheteria dos principais filmes
 </br>1. A cada linha somamos o valor da arrecadação à variável "gross", em seguida dividimos o total pelo tamanho do dataset para encontrar a média.
 </br>
  </br>
3.3 Etapa 3: Ator/Atriz com maior media de receita de bilheteria por filme
 </br>1. A mesma lógica da Etapa 1 se aplica aqui
 </br>
  </br>

3.4 Etapa 4: Quantas vezes o filme nº1 apareceu
 </br>1. Vamos criar dicionário vazio para armazenar nome do filme como chave e valor do contador como variável
 </br>2. Vamos criar a variável "movie" [string] para armazenar o nome do filme na linha analizada, se o filme já constar no dicionário recem criado, adicionamos 1 ao valor do contador
 </br>3.Caso o filme ainda não conste no dicionário recem criado, adicionamos ele como uma chave nova e iniciamos seu contador para 1, pois acabamos de vê-lo pela primeira vez
 </br>4. Criar um dicionário contendo as chaves e valores do "counts", mas ordenados pelo número de vezes que o filme apareceu na lista
 </br>5. A questão também pede que seja incluida o "rank" do filme na lista, por isso iniciamos o contador em 1 (o filme com mais aparições será o 1º) e acada loop será incrementado em 1
 </br>6. Basta passar por cada elemento da lista counts_sorted para termos a resposta
 </br>7. Mesma lógica da Etapa 4, mas dessa vez em vez de contar as aparições, vamos atribuir o valor total da receita como o valor da chave "Atores" para organizar o dicionário a partir dele
 </br>
 </br>




# Evidências


Gráficos plotados nas análises do Desafio


1.[Evidencias](/sprint_03/Evidencias)



# Certificados


- Certificado do Curso ABC
  
1.[Certificado AWS](/sprint_03/Certificados)
