FROM python:3.8-slim

# Evita prompts en instalaciones
ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependencias del sistema
RUN apt-get update && \
    apt-get install -y ffmpeg libsndfile1 git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Crear carpeta de trabajo
WORKDIR /app

# Copiar requirements e instalarlos antes que el código para aprovechar cache
COPY app/requirements.txt .

# Instalar dependencias de Python
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY app/ .

# Exponer puerto del servidor Flask
EXPOSE 5000

# Comando de inicio del servidor
CMD ["python", "main.py"]