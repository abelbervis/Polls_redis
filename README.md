# Polls_redis

_Django application counter views using redis cache, send mail using rabbitMQ_

### Pre-requisitos 📋

_Docker,Docker-compose, Git_

### Instalación 🔧

_dentro de la carpeta del proyecto, para iniciar los contenedores, use el comando:_

```
docker-compose up -- build
```

_abrir el navegador con la siguiente url:_

```
http://localhost:8000/polls/
```

_nos mostrara la ventana inicial del proyecto, donde veremos las preguntas que se encuentran en la BD postgres, con su cantidad de vistas y un formulario para enviar email usando redis rabbitMQ_
_para agregar una pregunta click en add question nos aparecera un login, necesitamos crear un super usuario:_
```
python manage.py createsuperuser 
```
_pagregamos su password y username y una vez creado podemos acceder al login de admin django y podemos agregar nuevas preguntas_
## Ejecutando las pruebas ⚙️


## Construido con 🛠️
* Django, Python
* Docker, Docker-compose
* Redis
* Celery
* RabbitMQ
* Bootstrap4

## Autor ✒️

* **Abel Bervis** 

