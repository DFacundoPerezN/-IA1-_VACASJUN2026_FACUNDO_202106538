from fastapi import FastAPI
from repositories.prolog_repo import PrologRepo
from controllers.city_controller import cities_router
from services.city_service import CityService

app = FastAPI(title="API de Ciudades y Rutas")

repository = PrologRepo("citys.pl")

service = CityService(repository)

app.include_router(cities_router(service))