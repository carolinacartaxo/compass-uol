# Usando uma imagem base com Python
FROM python:3.9-slim

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando o script Python do meu computador para o container
COPY hash_generator.py .

# Comandos para executar o script
CMD ["python", "hash_generator.py"]
