# Exercício de Geração de dados 

# Etapa 1: Em Python, declare e inicialize uma lista contendo 250 inteiros obtidos de forma aleatória. 
# Após, aplicar o método reverse sobre o conteúdo da lista e imprimir o resultado

# Etapa 2: Em Python, declare e inicialize uma lista contendo o nome de 20 animais. Ordene-os em ordem crescente e itere sobre os itens, imprimindo um a um (você pode utilizar list compreension aqui). 
# Na sequência, armazene o conteúdo da lista em um arquivo de texto, um item em cada linha, no formato CSV

import random

# Gerar uma lista de 250 inteiros aleatórios
numeros_aleatorios = [random.randint(0, 1000) for _ in range(250)]

# Reverter a lista
numeros_aleatorios.reverse()

# Imprimir o resultado
print(numeros_aleatorios)

# Lista de 20 animais
animais = ['Leão', 'Tigre', 'Elefante', 'Zebra', 'Girafa', 'Cavalo', 'Cachorro', 'Gato', 'Coelho', 'Rinoceronte',
           'Hipopótamo', 'Leopardo', 'Pantera', 'Urso', 'Lobo', 'Raposa', 'Panda', 'Formiga', 'Canguru', 'Cobra']

# Ordenar a lista em ordem crescente
animais.sort()

# Imprimir os nomes um a um
[print(animal) for animal in animais]

# Armazenar os nomes em um arquivo CSV
with open('animais.csv', 'w') as arquivo:
    for animal in animais:
        arquivo.write(f"{animal}\n")