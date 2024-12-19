# Usa la imagen oficial de Python
FROM python:3.10-slim

# Install PostgreSQL development libraries and other dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos al contenedor
COPY requirements.txt requirements.txt

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código del proyecto al contenedor
COPY . .

# Expone el puerto 8000 (por defecto para Django)
EXPOSE 8000

# Comando para iniciar el servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
