# Use a imagem base do Python
FROM python:3

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie todos os arquivos do diretório local para o diretório de trabalho do contêiner
COPY . /app

# Instale as dependências necessárias
RUN pip install -r requirements.txt

# Defina o comando a ser executado ao iniciar o contêiner
CMD ["python", "app.py"]

