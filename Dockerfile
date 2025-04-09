# Usa uma imagem Python
FROM python:3.10-slim

# Cria e usa um diretório de trabalho
WORKDIR /app

# Copia os arquivos para o container
COPY . .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 10000
EXPOSE 10000

# Comando para rodar o app com Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
