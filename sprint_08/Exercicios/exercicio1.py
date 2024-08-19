# Elaborar um código Python para gerar um dataset de nomes de pessoas.

import random
import names

# Definir os parâmetros
random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

# Gerar nomes únicos e armazenar na lista 'aux'
aux = []
for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())

# Gerar nomes aleatórios e armazenar na lista 'dados'
print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))
dados = []
for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

# Escrever os nomes em um arquivo de texto
with open('nomes_aleatorios.txt', 'w') as arquivo:
    for nome in dados:
        arquivo.write(f"{nome}\n")

print("Arquivo 'nomes_aleatorios.txt' gerado com sucesso!")
