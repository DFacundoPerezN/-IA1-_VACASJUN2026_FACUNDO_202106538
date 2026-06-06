from fastapi import APIRouter, Body
from services.city_service import CityService

def cities_router(service: CityService) -> APIRouter:
    router = APIRouter(prefix="/ciudades", tags=["ciudades"])

    @router.get("/", summary="Obtener todas las ciudades")
    def get_cities():
        return service.get_cities()


    @router.post("/", summary="Agregar una nueva ciudad")
    def add_city(data: dict = Body(...)):
        print(f"Datos recibidos para agregar ciudad: {data}")
        city = data.get("city")
        if not city:
            return {
                "success": False,
                "message": "El campo 'city' es requerido.",
                "code": 400
            }
        if not isinstance(city, str) or not city.strip():
            return {
                "success": False,
                "message": "El campo 'city' debe ser una cadena de texto.",
                "code": 400
            }
        return service.add_city(city)

    return router