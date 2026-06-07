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
    
    @router.post("/ruta", summary="Agregar una nueva ruta entre dos ciudades")
    def add_route(data: dict = Body(...)):
        print(f"Datos recibidos para agregar ruta: {data}")
        city1 = data.get("city1")
        city2 = data.get("city2")
        distance = data.get("distance")

        if not all([city1, city2, distance]):
            return {
                "success": False,
                "message": "Los campos 'city1', 'city2' y 'distance' son requeridos.",
                "code": 400
            }
        if not isinstance(city1, str) or not city1.strip() or not isinstance(city2, str) or not city2.strip():
            return {
                "success": False,
                "message": "Campos 'city1' y 'city2' deben ser cadenas de texto.",
                "code": 400
            }
        if not isinstance(distance, int) or distance <= 0:
            return {
                "success": False,
                "message": "El campo 'distance' debe ser un número entero positivo.",
                "code": 400
            }
        if city1.lower() == city2.lower():
            return {
                "success": False,
                "message": "Las ciudades 'city1' y 'city2' no pueden ser la misma.",
                "code": 400
            }
        return service.add_route(city1, city2, distance)

    @router.get("/mejor_ruta", summary="Obtener la mejor ruta entre dos ciudades")
    def get_best_route(city1: str, city2: str): 

        if not city1.strip() or not city2.strip():
            return {
                "success": False,
                "message": "Los parámetros 'city1' y 'city2' no pueden estar vacíos.",
                "code": 400
            }
        
        return service.get_best_route(city1, city2)
    
    @router.get("/recorridos", summary="Obtener todos los recorridos entre dos ciudades")
    def get_all_routes(city1: str, city2: str):
        if not city1.strip() or not city2.strip():
            return {
                "success": False,
                "message": "Los parámetros 'city1' y 'city2' no pueden estar vacíos.",
                "code": 400
            }
        
        return service.get_all_routes(city1, city2)

    return router