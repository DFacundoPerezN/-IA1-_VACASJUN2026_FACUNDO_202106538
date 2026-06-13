# Manual Técnico

## Prolog

Prolog es el corazón de este sistema ya es donde se guarda toda la información para las consultas, también es donde se relizan las operaciones para la logica de las conclusiones llegadas por inferencia.

### Hechos y reglas

Guardamos la informacion con hechos, como por ejemplo las ciudades son hechos atomicos por ser indivisibles, mientras que las conexiones requieren parametros.

```prolog
% Sintomas
sintoma(pantalla_negra).
sintoma(reinicio_inesperado).

falla(sobrecalentamiento_procesador).
falla(disco_duro_lastimado).
falla(memoria_ram_defectuosa).

recomendacion(actualizar_sistema_operativo).
```

tenemos la conexion entre sintomas y falla

```prolog
falla_causada_por(sobrecalentamiento_procesador, [temperatura_elevada, ruido_desconocido, reinicio_inesperado]).


tenemos la conexion entre falla y recomendaciones

```prolog
tratamiento(memoria_ram_defectuosa, [ejecutar_diagnostico_ram, limpiar_contactos]).
```

### Diagnostico

para el diagnostico buscamos la falla con el listado de sintomas minimos, incluimos un **corte** verde.

```prolog
diagnosticar(ListaSintomasUsuario, Falla) :-
    falla_causada_por(Falla, SintomasRequeridos),
    subset(SintomasRequeridos, ListaSintomasUsuario), !.
```

### Dar recomendaciones segun listado de sintomas

Ahora para encontramos el diagnositoco de la falla y segun esta encontramos los sintomas disponibles

```prolog
% Regla para obtener recomendaciones según síntomas
obtener_recomendaciones(ListaSintomasUsuario, Recomendaciones) :-
    diagnosticar(ListaSintomasUsuario, Falla),
    tratamiento(Falla, Recomendaciones).
```

### Usar más de un archivo para prolog

dpara esto definimos los mismos parametros para los hechos

```prolog
:- multifile ciudad/1.
:- multifile ruta/3.
```

## Backend en Python

Para el backend usamos un patron de arquitectura que nos permite dividir las consultas y la api en tres partes y el bot:

### Repositories

Consultas al repositorio

```python
from pyswip import Prolog
from pathlib import Path
import re
from typing import List

class PrologRepo:
    def __init__(self, prolog_file):
        self.prolog_file = Path(prolog_file).resolve()
        self.aux_file = Path("c_aux.pl").resolve()
        self.prolog = Prolog()
        self._consult_file()
```

```python
import repositories.prolog_repo as prolog_repo
from typing import List

class Recommendatios_Repo(prolog_repo.PrologRepo):

    def __init__(self, prolog_file):
        super().__init__(prolog_file)

    def get_recomendaciones(self) -> List[str]:
        sol = self.query_one("get_recomendaciones(Lista).")
        if not sol:
            return []
        return [str(falla) for falla in sol['Lista']]
```

### Servicios

Conecta repositories al exterior.

```python
from typing import List
from repositories.prolog_repo import PrologRepo
from repositories.sintoms_repo import SintomsRepo
from repositories.fails_repo import FailsRepo
from repositories.recommendations_repo import Recommendatios_Repo
from telegram.bot import TelegramBot 

class DoctorService:
    def __init__(self, prolog_repo: PrologRepo):
        self.prolog_repo = prolog_repo
        self.sintoms_repository = SintomsRepo(prolog_repo.prolog_file)
        self.fails_repository = FailsRepo(self.prolog_repo.prolog_file)
        self.recom_repository = Recommendatios_Repo(self.prolog_repo.prolog_file)
        self.bot = TelegramBot()

    def get_sintomas(self) -> List[str]:
        return self.sintoms_repository.get_sintomas()
    
    def get_falla_by_sintomas(self, listaSintomas: List, notificar= True) -> dict:
        response = self.fails_repository.get_falla_por_sintomas(listaSintomas)
        if (notificar):
            if (response["falla"] is not None ) and (response["falla"] != []):
                self.bot.enviar_falla(listaSintomas, response["falla"])
        return response
```

### Controllers

Expone las funciones, que llama desde service a la API

```python
from fastapi import APIRouter, Body
from services.doctor_service import DoctorService

def doctor_router(service: DoctorService) -> APIRouter:
    router = APIRouter(prefix="/doctor", tags=["doctor"])
    
    @router.get("/sintomas", summary="Obtener todos los síntomas")
    def get_sintomas():
        return service.get_sintomas()
    
    @router.get("/all_fallas", summary="Obtener todos las fallas")
    def get_all_fallas():
        return service.get_all_fallas()
```

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

## Frontend

Para este proyecto se opcto por un sitio web estatico con una arquitectura que se divide asi:

```text
frontend/
├── index.html
├── admin.html
├── css/
│   └── styles.css   (¡Nuevo archivo para el estilo oscuro!)
└── js/
    ├── api.js
    └── main.js
    └── admin.js
```

### index.html

Este archivo es el que tiene toda la imagen princiapal de la pagina web tiene toda la estructura y los llamados y usos de los demas archivos.

### admin.html

Este archivo es el que toda las opciones del administrador.

### style.css

Hoja de estilos para la pagina web.

### main.js

Este archivo es el que tiene la logica de la pagina web princiapal llama a las instrucciones de api.js para que sea visible en la pagina web.

### admin.js

Este archivo es el que tiene la logica de la pagina de administrador llama a las instrucciones de api.js para el administrador.

### api.js

Este archivo hace las conxiones con la API de python la cual devuelve la información necesaria.

## Arquitectura

Presentamos el diagrama de arquitectura donde el usuario hace consultas desde el navegador, el navegdor corre el frontent que envia por medio de una REST-APi la informacion al backend, este hace las consutlas necesarias al archivo de prolog. Los diagnosticos que son enviados con información pueden ser enviados al bot de prolog apar que notifique y envie la información a un chat, esto solo si esta activada la notificación.

![Diagrama de arquitectura](/Proyecto1/doc/img/Arquitectura_IA.drawio.png)
