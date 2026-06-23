# py -3.10 -m venv venv
# .\venv\Scripts\Activate.ps1
# pip install fastapi uvicorn base
# pip install --no-cache-dir -r requirements.txt
# uvicorn main:app --reload
"""
Punto de entrada de la aplicación RoboMaze (backend).

Para ejecutar en desarrollo:
    uvicorn app.main:app --reload
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import router

app = FastAPI(
    title="RoboMaze API",
    description="API REST para resolver laberintos con BFS y DFS",
    version="1.0.0",
)

# CORS habilitado para permitir que el frontend (React, en otro puerto/origen)
# pueda consumir la API durante desarrollo.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def root():
    return {"message": "RoboMaze API está corriendo. Visita /docs para ver la documentación."}