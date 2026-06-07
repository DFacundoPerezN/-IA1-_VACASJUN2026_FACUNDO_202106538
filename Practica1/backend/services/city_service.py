from typing import List
from repositories.prolog_repo import PrologRepo

class CityService:
    def __init__(self, city_repository: PrologRepo):
        self.city_repository = city_repository
    
    def get_cities(self) -> List[dict]:
        return self.city_repository.get_ciudades()
    
    def add_city(self, city_name: str) -> dict:
        return self.city_repository.agregar_ciudad(city_name.lower())
    
    def add_route(self, city1: str, city2: str, distance: int) -> dict:
        return self.city_repository.agregar_ruta(city1.lower(), city2.lower(), distance)
    
    def get_best_route(self, city1: str, city2: str) -> dict:
        return self.city_repository.obtener_mejor_ruta(city1.lower(), city2.lower())
    
    def get_all_routes(self, city1: str, city2: str) -> List[dict]:
        return self.city_repository.obtener_recorridos(city1.lower(), city2.lower())