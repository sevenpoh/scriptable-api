FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# Instala dependências do sistema necessárias para o Playwright rodar com Chromium
RUN apt-get update && apt-get install -y \
    wget gnupg \
    libnss3 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libdrm2 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libxshmfence1 \
    libx11-xcb1 \
    libxext6 \
    libxfixes3 \
    libxi6 \
    libxcursor1 \
    libxrender1 \
    libxss1 \
    libxtst6 \
    fonts-liberation \
    libu2f-udev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Instala o Chromium usado pelo Playwright
RUN python -m playwright install

# Copia o restante dos arquivos para dentro do container
COPY . .

# Define o comando padrão ao iniciar o container
CMD ["python", "main.py"]
