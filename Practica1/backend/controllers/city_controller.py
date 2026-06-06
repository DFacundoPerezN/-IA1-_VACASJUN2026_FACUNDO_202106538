from fastapi import APIRouter, Body
from services.city_service import CityService

def cities_router(service: CityService) -> APIRouter:
    router = APIRouter(prefix="/ciudades", tags=["ciudades"])

    @router.get("/", summary="Obtener todas las ciudades")
    def get_cities():
        return service.get_cities()


    return router