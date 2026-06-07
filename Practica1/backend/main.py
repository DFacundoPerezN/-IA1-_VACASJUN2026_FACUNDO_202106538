# py -3.10 -m venv venv
# .\venv\Scripts\Activate.ps1
# pip install fastapi uvicorn pyswip
# uvicorn main:app --reload
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from repositories.prolog_repo import PrologRepo
from controllers.city_controller import cities_router
from services.city_service import CityService

app = FastAPI(title="API de Ciudades y Rutas")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite peticiones desde cualquier origen (para desarrollo)
    allow_credentials=True,
    allow_methods=["*"],  # Permite GET, POST, etc.
    allow_headers=["*"],
)

repository = PrologRepo("citys.pl")

service = CityService(repository)

app.include_router(cities_router(service))