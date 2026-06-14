# Manual Técnico

## SmartBot

Sistema de respuestas automatizadas basado en Telegram

## Backend en Python

Para el backend usamos un patron de arquitectura que nos permite dividir las consultas y la api en tres partes y el bot. podriamos resumir las tecnologias usadas en el backend como:

- Python
- Flask
- MongoDB
- PyMongo

### Routes

Se encargan de las operaciones de exponer API y comunicar con las funciones de MongoDB

```python
categories_bp = Blueprint(
    "categories",
    __name__,
    url_prefix="/categories"
)

@categories_bp.route("", methods=["GET"])
def get_categories():

    categories = []

    for category in db.categories.find():

        categories.append({
            "id": str(category["_id"]),
            "name": category["name"]
        })
```

### Servicios

En esta practica los servicios eran lso encartgados de las accioens y comunicacion del bot con telegram.

- telegram_listener para comunicacion asincrona
- telegram_service para trabajo del bot

### Database

Esto es para que se logre conectar a la instancia de MongoDB, se eligio mongo db por la practicalidad con el tipo de datos y consultas a hacer.

### Bot

El bot es el que maneja los mensjaes de notificacion al chat.

```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

class TelegramBot:
    def __init__(self):
        self.token = TOKEN
        self.chat_id = CHAT_ID
```

Tambien tiene un apartado de listener para estar al pendiente de las preguntas y hacer consultas al endpoint que ocnecta con la base de preguntas.

## Frontend

Para este proyecto se opcto por un sitio web construido con los siguientes frameworks:

- React
- Vite
- Axios

## Infraestructura y docker

Se utilizo docker para la construcción de imagenes a partir del backend, frontend y la base de datos.

```Dockerfile
FROM node:22-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]
```

Estos contenedores son construidos y levantados desde un docker compose que sirve como controlador de puertos y conexiónes entre estos contenedores.

```yaml
services:

  mongo:
    image: mongo:8
    container_name: smartbot-mongo

    ports:
      - "27017:27017"

    environment:
      ...

    volumes:
      - mongo_data:/data/db

  backend:
    build:
      context: ./backend

    container_name: smartbot-backend

    ports:
      - "5000:5000"

    depends_on:
      - mongo

    environment:
      - ...
  frontend:
    build:
      context: ./frontend

    container_name: smartbot-frontend

    ports:
      - "5173:5173"

    depends_on:
      - backend
```

## Arquitectura

Presentamos el diagrama de arquitectura donde el administrador hace consultas desde el navegador, el navegdor corre el frontent que envia por medio de una REST-APi la informacion al backend, este hace las consutlas necesarias a la base de datos.
Por otra parte el usuario común usa comunicación con el bot de telegram para hacer preguntas que hacen al bot usar un endpoint que comunica con la base de datos de prolog.

![Diagrama de arquitectura](/Practica2/documentation/Arquitectura.png)