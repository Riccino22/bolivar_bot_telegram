# install google chrome
# Usa una imagen base de Python
FROM python:3.9-slim

# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Instalar Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# Instalar ChromeDriver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Establecer la variable de entorno DISPLAY para evitar errores
ENV DISPLAY=:99

# Copiar el archivo requirements.txt en el contenedor
COPY requirements.txt /app/requirements.txt

# Instalar las dependencias del proyecto
RUN pip install -r /app/requirements.txt

# Copiar los archivos del proyecto al contenedor
COPY . /app

# Establecer el directorio de trabajo
WORKDIR /app

# Exponer el puerto
EXPOSE 5000

# Comando para correr la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

