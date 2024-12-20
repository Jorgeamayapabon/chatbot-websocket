FROM python:3.10-alpine

WORKDIR /app

# Copia el archivo de requisitos al contenedor
COPY requirements.txt requirements.txt

# Instala las dependencias
RUN pip3 install --no-cache-dir -r requirements.txt

# Copia el código del proyecto al contenedor
COPY . .

# Expone el puerto 8000 (por defecto para Django)
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
