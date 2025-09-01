# Dockerfile

# 1. Imagem base:
FROM python:3.12.10

# 2. Diretório de trabalho: Define o diretório onde o código será executado dentro do contêiner.
WORKDIR /app

# 3. Dependências do sistema: OpenCV pode precisar de algumas bibliotecas do sistema.
#    Esta é uma etapa crítica para evitar erros de "import cv2".
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 4. Copie o arquivo de dependências primeiro para aproveitar o cache do Docker.
COPY requirements.txt .

# 5. Instale as dependências Python.
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copie todo o resto do código da aplicação para o contêiner.
COPY . .

# 7. Exponha a porta padrão do Streamlit.
EXPOSE 8501

# 8. Comando para iniciar a aplicação quando o contêiner rodar.
CMD ["streamlit", "run", "app.py"]