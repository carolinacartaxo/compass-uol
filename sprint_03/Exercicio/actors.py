column, dataset = [], []
# Abrir arquivo .CSV
with open ('actors.csv') as file:
    # Criar variavel para receber conteudo do arquivo, splitlines separa as linhas
    reader = file.read().splitlines()
    # Criar uma lista 'coluna' para receber os nomes dos cabeçalhos, estes serão usados para criar as chaves dos dicionários
    for line in reader:
        if line == reader[0]:
            tmp = line.split(',')
            for word in tmp:
                column.append(word)
        # A partir da linha[1], pegar os valores da tabela. Cada linha do arquivo será combinado com o cabeçalho para criar um dicionário
        else:
            tmp = line.split(',')
            value = {}
            # Caso algum dos valores possua vírgula que não signifique divisão entre tabelas, devemos encontrar o valor problemático e assegurar que ele apareça em uma única coluna
            if len(tmp) > 6:
                n, w = [], []
                # Vasculhar cada caractere da linha problemática em busca de " " pois estes simbolizam que tudo pertence a uma coluna, apesar da vírgula
                for i in range(len(line)):
                    a = list(line)
                    # Caso algum caractere seja encontrado, salvaremos a posição [integer] dele na lista n
                    if a[i] == '\"':
                        n.append(i)
                # Se n for igual a 2, encontramos a palavra. Devemos: 
                # 1. colocar a palavra encontrada em substring, 2. Separar o resto da linha em lista por vírgula 3. Concatenar a palavra e a lista em um único dicionário
                if len(n) == 2:
                    x = line[n[0]:(n[1] + 1)]
                    y = line[(n[1] + 2):(len(line) + 1)].split(',')
                    w.append(x)
                    for i in range(len(y)):
                        w.append(y[i])
                # Cada coluna é acrescentada ao dicionário vazio "Value" por meio da variável insert
                for i in range (0, len(w)):
                    insert = {f'{column[i]}': f'{w[i]}'}
                    value.update(insert)
                # Ao final do loop da linha, devemos adicionar o dicionário "Value" na lista dataset para montar a nossa base de dados
                dataset.append(value)
            else:
                for i in range (len(tmp)):
                    insert = {f'{column[i]}': f'{tmp[i]}'}
                    value.update(insert)
                dataset.append(value)

#3.1 Etapa 1: Nome do ator/atriz com maior número de filmes e respectiva quantidade
name = ''
count = 0
# A cada linha comparamos o valor do número de filmes com o valor do contador, caso seja superior, atualizamos o contador e salvamos o nome do ator. Depois basta imprimir as duas variáveis
for i in dataset:
    x = int(i.get('Number of Movies'))
    if x > count:
        count = x
        name = i.get('Actor')
print(f'{name} com {count} filmes')

with open ('etapa-1.txt', 'w') as file:
    file.write(f'{name} com {count} filmes')

#3.2 Etapa 2: Média de bilheteria dos principais filmes
name = ''
gross = 0
# A cada linha somamos o valor da arrecadação à variável "gross", em seguida dividimos o total pelo tamanho do dataset para encontrar a média.
for i in dataset:
    gross += float(i.get('Gross'))
print('A média de bilheteria dos principais filmes é de {:.2f} milhões de dólares'.format((gross / len(dataset))))

with open ('etapa-2.txt', 'w') as file:
    file.write('A média de bilheteria dos principais filmes é de {:.2f} milhões de dólares'.format((gross / len(dataset))))

#3.3 Etapa 3: Ator/Atriz com maior media de receita de bilheteria por filme
name = ''
count = 0
# Mesma lógica da Etapa 1 se aplica aqui
for i in dataset:
    x = float(i.get('Average per Movie'))
    if x > count:
        count = x
        name = i.get('Actor')
print('{} com a média de {:.2f} milhões de dólares por filme'.format(name, count))

with open ('etapa-3.txt', 'w') as file:
    file.write('{} com a média de {:.2f} milhões de dólares por filme'.format(name, count))

#3.4 Etapa 4: Quantas vezes o filme nº1 apareceu
# 1. Criar dicionário vazio para armazenar nome do filme como chave e valor do contador como variável
counts = {}
for i in dataset:
    # Criar variável "movie" [string] para armazenar o nome do filme na linha analizada, se o filme já constar no dicionário recem criado, adicionamos 1 ao valor do contador
    movie = i.get("#1 Movie")
    if movie in counts:
        counts[movie] += 1
    # Caso o filme ainda não conste no dicionário recem criado, adicionamos ele como uma chave nova e iniciamos seu contador para 1, pois acabamos de vê-lo pela primeira vez
    else:
        counts[movie] = 1

# Criar um dicionário contendo as chaves e valores do "counts", mas ordenados pelo número de vezes que o filme apareceu na lista
counts_sorted = {k: v for k, v in sorted(counts.items(), key=lambda x: x[1], reverse=True)}
# A questão também pede que seja incluida o "rank" do filme na lista, por isso iniciamos o contador em 1 (o filme com mais aparições será o 1º) e acada loop será incrementado em 1
position = 1
# Basta passar por cada elemento da lista counts_sorted para termos a resposta
with open ('etapa-4.txt', 'w') as file:
    for movie in counts_sorted:
        file.write(f'{position} - O filme {movie} aparece {counts_sorted[movie]} vez(es) no dataset\n')
        print(f'{position} - O filme {movie} aparece {counts_sorted[movie]} vez(es) no dataset')
        position += 1

#3.5 Etapa 5: Lista ordenada de atores por bilheteria (Total Gross) em ordem decrescente:
total_gross = {}
# Mesma lógica da Etapa 4, mas dessa vez em vez de contar as aparições, vamos atribuir o valor total da receita como o valor da chave "Atores" para organizar o dicionário a partir dele
for i in dataset:
    actor = i.get('Actor')
    gross = float(i.get('Gross'))
    total_gross[actor] = gross
tg_sorted = {k: v for k, v in sorted(total_gross.items(), key=lambda x: x[1], reverse=True)}

with open ('etapa-5.txt', 'w') as file:
    for actor in tg_sorted:
        file.write(f'{actor} - {tg_sorted[actor]}\n')
        print(f'{actor} - {tg_sorted[actor]}')