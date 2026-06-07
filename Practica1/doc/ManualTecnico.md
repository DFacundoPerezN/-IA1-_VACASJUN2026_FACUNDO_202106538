# Manual Técnico

## Prolog

Prolog es el corazón de este sistema ya es donde se guarda toda la información para las consultas, también es donde se relizan las operaciones para el calculo de las rutas.

### Hechos y reglas

Guardamos la informacion con hechos, como por ejemplo las ciudades son hechos atomicos por ser indivisibles, mientras que las conexiones (o rutas) requieren dos ciudades y una distancia.

```prolog
ciudad(berlin).
ciudad(hamburgo).
ruta(essen, dortmund, 36).
ruta(dortmund, bremen, 235).
```

para calcular la distacia entre dos ciudades usamos el hecho de ruta.

```prolog
ciudad(berlin).
ciudad(hamburgo).
ruta(essen, dortmund, 36).
ruta(dortmund, bremen, 235).
```

### Busqueda entre rutas con reglas

para la busqueda primero definimos las ciudades que necesitamos conectar y las salidas de Lista de ciudades (camino) y distancia total.

```prolog
recorrido(Origen, Destino, ListaCiudades, Distancia) :-
    recorrido_aux(Origen, Destino, [Origen], ListaCiudades, Distancia).

% Base: Una ruta directa entre el Origen y el Destino.
recorrido_aux(Origen, Destino, Visitadas, ListaCiudades, Distancia) :-
    distancia(Origen, Destino, Distancia),

    % Construr lista final append al destino
    append(Visitadas, [Destino], ListaCiudades).
```

Para la segunda parte manejamos un historial de ciudades vistas para evitar qeu se encicle y que vaya dos veces a la misma ciudad

```prolog
% Recursion: No hay ruta directa, buscamos una ciudad intermedia (Siguiente).
recorrido_aux(Origen, Destino, Visitadas, ListaCiudades, Distancia) :-
    distancia(Origen, Siguiente, D1),

    % Evitamos ciclos al confirmar que Siguiente no haya sido visitada antes
    \+ member(Siguiente, Visitadas),
    % Evitamos pasar dos veces por el Destino
    \+ member(Destino, Visitadas),

    % Añadimos la ciudad intermedia a los Visitadas
    append(Visitadas, [Siguiente], NuevosVisitadas),

    % Buscamos el resto del camino desde 'Siguiente' hasta el 'Destino'
    recorrido_aux(Siguiente, Destino, NuevosVisitadas, ListaCiudades, D2),
    % Sumar distancias
    Distancia is D1 + D2.
```

### Ruta más corta

```prolog
mejor_ruta(Origen, Destino, MejorCamino, MenorDistancia) :-
    % Encontrar Todas las combinaciones de caminos y distancias
    % Guardamos parejas del formato: r(Distancia, Camino)
    findall(r(Dist, Camino), recorrido(Origen, Destino, Camino, Dist), TodasLasRutas),
    
    % Seleccionar la que tiene la menor distancia
    obtener_minima(TodasLasRutas, r(MenorDistancia, MejorCamino)).
```

Si solo hay una ruta se usa ! para que no busque mas rutas.

```prolog
obtener_minima([Ruta], Ruta) :- !.
```

Comparar la primera ruta con la menor del resto de la lista. para esto hacemos un if then else:

```prolog
obtener_minima([r(D1, C1) | Resto], r(MinD, MinC)) :-
    obtener_minima(Resto, r(D2, C2)),
    (D1 < D2 -> 
        MinD = D1, MinC = C1 
    ; 
        MinD = D2, MinC = C2
    ).
```

### Usar más de un archivo para prolog

dpara esto definimos los mismos parametros para los hechos

```prolog
:- multifile ciudad/1.
:- multifile ruta/3.
```

## Backend en Python

Para el backend usamos un patron de arquitectura que nos permite dividir las consultas y la api en tres partes:

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
    def get_ciudades(self) -> List[str]:
        sol = self.query_one("get_ciudades(Lista)")
        if not sol:
            return []
        return [str(ciudad) for ciudad in sol['Lista']]
```

### Servicios

Conecta repositories al exterior.

```python
from typing import List
from repositories.prolog_repo import PrologRepo

class CityService:
    def __init__(self, city_repository: PrologRepo):
        self.city_repository = city_repository
    
    def get_cities(self) -> List[dict]:
        return self.city_repository.get_ciudades()
```

### Controllers

Expone las funciones, que llama desde service a la API

```python
from fastapi import APIRouter, Body
from services.city_service import CityService

def cities_router(service: CityService) -> APIRouter:
    router = APIRouter(prefix="/ciudades", tags=["ciudades"])

    @router.get("/", summary="Obtener todas las ciudades")
    def get_cities():
        return service.get_cities()

    return router
```

## Frontend

Para este proyecto se opcto por un sitio web estatico con una arquitectura que se divide asi:

```text
frontend/
├── index.html
├── css/
│   └── styles.css   (¡Nuevo archivo para el estilo oscuro!)
└── js/
    ├── api.js
    └── main.js
```

### index.html

Este archivo es el que tiene toda la imagen de la pagina web tiene toda la estructura y los llamados y usos de los demas archivos.

### style.css

Hoja de estilos para la pagina web.

### main.js

Este archivo es el que tiene toda la logica de la pagina web llama a las instrucciones de api.js para que sea visible en la pagina web.

### api.js

Este archivo hace las conxiones con la API de python la cual devuelve la información necesaria.
