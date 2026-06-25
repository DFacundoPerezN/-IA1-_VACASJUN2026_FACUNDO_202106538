# Manual Técnico RoboMaze

Aplicación web para visualizar algoritmos de búsqueda (BFS, DFS y A*) sobre laberintos interactivos. El usuario dibuja el laberinto en el navegador, ejecuta un algoritmo y observa en tiempo real cómo el agente explora el espacio y encuentra la ruta.

---

## Requisitos

- Python 3.10 o superior
- Node.js 18 o superior
- npm 9 o superior

---

## Instalación y ejecución

### Backend

```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload
```

El servidor queda disponible en `http://127.0.0.1:8000`.  
La documentación interactiva (Swagger) en `http://127.0.0.1:8000/docs`.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

La interfaz queda disponible en `http://localhost:5173`.

---

## Estructura del proyecto

```txt
robomaze/
├── backend/
│   ├── app/
│   │   ├── domain/              # Modelos del dominio
│   │   │   ├── cell.py          # Representa una celda (fila, columna)
│   │   │   ├── maze.py          # Cuadrícula, validaciones y vecinos
│   │   │   └── search_result.py # Resultado de un algoritmo
│   │   ├── models/          # Implementaciones de búsqueda
│   │   │   ├── base.py          # Interfaz Strategy (SearchAlgorithm)
│   │   │   ├── bfs.py           # Breadth-First Search
│   │   │   ├── dfs.py           # Depth-First Search
│   │   │   ├── astar.py         # A* con heurística Manhattan
│   │   │   ├── heuristics.py    # Función de distancia Manhattan
│   │   │   └── factory.py       # Factory para instanciar algoritmos
│   │   ├── services/
│   │   │   └── maze_search_service.py  # Orquesta casos de uso
│   │   ├── api/
│   │   │   ├── routes.py        # Endpoints REST (FastAPI)
│   │   │   └── schemas.py       # DTOs con validación Pydantic
│   │   └── main.py              # Arranque de la aplicación y CORS
│   ├── tests/
│   │   └── test_algorithms.py   # 13 tests unitarios
│   └── requirements.txt
├── frontend/
│   └── src/
│       ├── api/
│       │   └── mazeApi.js       # Llamadas HTTP al backend (axios)
│       ├── components/
│       │   ├── MazeGrid.jsx     # Cuadrícula interactiva
│       │   ├── Controls.jsx     # Panel de modos y botones
│       │   └── Results.jsx      # Panel de resultados
│       ├── hooks/
│       │   └── useMaze.js       # Estado global y lógica del laberinto
│       └── App.jsx              # Componente raíz
└── README.md
```

---

## API REST

Base URL: `http://127.0.0.1:8000/api`

### `GET /algorithms`

Devuelve los algoritmos disponibles.

**Respuesta:**

```json
{ "algorithms": ["bfs", "dfs", "astar"] }
```

---

### `POST /search`

Ejecuta un algoritmo sobre el laberinto enviado.

**Body:**

```json
{
  "rows": 10,
  "cols": 10,
  "start":  { "row": 0, "col": 0 },
  "goal":   { "row": 9, "col": 9 },
  "obstacles": [{ "row": 1, "col": 1 }, { "row": 1, "col": 2 }],
  "algorithm": "bfs"
}
```

**Respuesta:**

```json
{
  "algorithm": "BFS",
  "found": true,
  "path": [{ "row": 0, "col": 0 }, "..."],
  "path_length": 18,
  "explored_order": ["..."],
  "nodes_explored": 45,
  "execution_time_ms": 0.312
}
```

---

### `POST /compare`

Ejecuta BFS y DFS sobre el mismo laberinto y devuelve ambos resultados.

**Body:** igual que `/search` pero sin el campo `algorithm`.

---

## Arquitectura del backend

Se aplica una **arquitectura por capas** con separación clara de responsabilidades:

```txt
API (routes.py)
    ↓  recibe HTTP, valida con Pydantic
Service (maze_search_service.py)
    ↓  orquesta el caso de uso
Factory (factory.py)
    ↓  instancia el algoritmo solicitado
Algorithm (bfs / dfs / astar)
    ↓  ejecuta la búsqueda sobre el dominio
Domain (maze.py, cell.py, search_result.py)
       modelos puros sin dependencias externas
```

Adicionalmente se aplica el **patrón Strategy**: todos los algoritmos implementan la interfaz `SearchAlgorithm` (método `search(maze) → SearchResult`), lo que permite intercambiarlos sin modificar el resto del sistema.

---

## Algoritmos implementados

### BFS — Breadth-First Search

Explora el laberinto nivel por nivel usando una **cola FIFO** (`collections.deque`). Garantiza encontrar la **ruta más corta** en número de pasos.

```txt
Complejidad temporal:  O(V + E)
Complejidad espacial:  O(V)
Ruta óptima:           Sí
```

### DFS — Depth-First Search

Explora tan profundo como sea posible antes de retroceder, usando una **pila LIFO**. No garantiza la ruta más corta.

```txt
Complejidad temporal:  O(V + E)
Complejidad espacial:  O(V)
Ruta óptima:           No
```

### A* — A Estrella

Usa una **cola de prioridad (min-heap)** y guía la búsqueda con la fórmula:

```txt
f(n) = g(n) + h(n)

g(n) → pasos reales desde el inicio hasta n
h(n) → distancia Manhattan desde n hasta el destino
```

Garantiza la ruta más corta y generalmente explora menos nodos que BFS gracias a la heurística.

```txt
Complejidad temporal:  O(V log V)
Complejidad espacial:  O(V)
Ruta óptima:           Sí
```

**Distancia Manhattan:**

```txt
h(n) = |fila_n - fila_destino| + |col_n - col_destino|
```

---

## Ejecutar tests

```bash
cd backend
python -m pytest tests/ -v
```

13 tests unitarios que cubren: rutas válidas, destinos inalcanzables, validaciones del laberinto, longitud óptima de ruta, contigüidad del camino y comparación de nodos explorados entre algoritmos.

---

## Uso de la interfaz

1. Ajusta el tamaño del laberinto con los campos **Filas** y **Columnas**.
2. Selecciona el modo **Inicio** y haz clic en una celda.
3. Selecciona el modo **Destino** y haz clic en otra celda.
4. Selecciona **Muro** y dibuja obstáculos haciendo clic o arrastrando.
5. Presiona **▶ BFS**, **▶ DFS** o **▶ A*** para ejecutar.
6. Observa la animación: las celdas azul claro son exploradas, las azul intenso forman la ruta final.
7. El panel derecho muestra la ruta completa, nodos explorados y tiempo de ejecución.

## Arquitectura

La arquitectura presenta a como el usuario se conecta con el frontend a través del navegador y como el frontend hace consultas API REST al backend donde se ejecuta la lógica de los algoritmos.

![Diagrama de arquitectura](/Practica4/doc/arquitectura.png)
