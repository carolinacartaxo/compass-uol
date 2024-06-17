# Explicação do Desafio 


## Etapa 1
Construa uma imagem a partir de um arquivo de instruções Dockerfile que execute o código `carguru.py`. Após, execute um container a partir da imagem criada.

### Criei o arquivo Dockerfile para `carguru.py` na mesma pasta do arquivo `carguru.py` com o seguinte script:

#### Usei uma imagem base com Python
`FROM python:3.9-slim`

#### Defini o diretório de trabalho dentro do container
`WORKDIR /app`

#### Copiei o script Python do meu computador para o container
`COPY carguru.py .`

#### Comandos que utilizei para a execução do script
`CMD ["python", "carguru.py"]`
</br>
</br>
</br>
Após a criação do script, rodei os seguintes comandos no terminal dentro do diretório dos arquivos:

#### Comando para construir a imagem Docker
`docker build -t carguru-image .`

#### Comando para executar o container
`docker run --name carguru-container carguru-image`

IMAGEM DO TERMINAL

## Etapa 2
É possível reutilizar containers? Em caso positivo, apresente o comando necessário para reiniciar um dos containers parados em seu ambiente Docker? Não sendo possível reutilizar, justifique sua resposta.

### Resposta:
Sim, é possível reutilizar containers.

#### O comando para reiniciar um container parado é: 
`docker start carguru-container`
#### O comando para reiniciar um container em execução é:
`docker restart carguru-container`

IMAGEM DO TERMINAL

## Etapa 3
Agora vamos exercitar a criação de um container que permita receber inputs durante sua execução.
#### 1. Criar novo script Python que implementa o algoritmo a seguir:
##### • Receber uma string via input.
##### • Gerar o hash da string por meio do algoritmo SHA-1.
##### • Imprimir o hash em tela, utilizando o método hexdigest.
##### • Retornar ao passo 1.

#### 2. Criar uma imagem Docker chamada mascarar-dados que execute o script Python criado anteriormente.

#### 3. Iniciar um container a partir da imagem, enviando algumas palavras para mascaramento.

#### 4. Registrar o conteúdo do script Python, arquivo Dockerfile e comando de inicialização do container neste espaço.

### Resolução:
Criei um arquivo python chamado `hash_generator` e neste eu importei a biblioteca hashlib para trabalhar com algoritmos de hash.

No código em comento, criei um loop infinito que receberá uma string como input do usuário e o vai gerar um hash da string no algoritmo SHA-1.

```
import hashlib

while True:
    user_input = input("Digite uma string para transformar em hash: ")
    hash_object = hashlib.sha1(user_input.encode())
    hex_dig = hash_object.hexdigest()
    print(f"SHA-1 hash: {hex_dig}")
```


Tal qual a etapa anterior, vou criar um arquivo Dockerfile no mesmo diretório do meu arquivo python com o seguinte script:

#### Usei uma imagem base com Python
`FROM python:3.9-slim`

#### Defini o diretório de trabalho dentro do container
`WORKDIR /app`

#### Copiei o script Python do meu computador para o container
`COPY hash_generator.py .`

#### Comandos utilizados para executar o script
`CMD ["python", "hash_generator.py"]` 

#### Comando utilizado para criar a imagem mascarar-dados:
`docker build -t mascarar-dados .`

IMAGEM DO TERMINAL

Aqui vamos iniciar o container de forma interativa para recebermos o input do usuário usando 
`docker run -it mascarar-dados`

IMAGEM DO TERMINAL
