#Creamos la base de la imagen de python
FROM python:3.9  

#Instalamos el SSH client
RUN apt-get update && apt-get install -y openssh-client

#Configuramos las vairables de entorno para python
ENV PYTHONUNBUFFERED 1

#Establecemos el directorio de trabajo
WORKDIR /app

#Copia el archivo requirements.txt de tu máquina local al contenedor
COPY requirements.txt /app/requirements.txt

#Instalamos las dependencias que estan en el archivo
RUN pip install -r requirements.txt

#Copia todo el contenido de tu maquina local al contenedor  
COPY . /app

#Comando para iniciar el servidor 
CMD python manage.py runserver 0.0.0.0:8000