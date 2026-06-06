from typing import List
from repositories.prolog_repo import PrologRepo

class CityService:
    def __init__(self, city_repository: PrologRepo):
        self.city_repository = city_repository
    
    def get_cities(self) -> List[dict]:
        return self.city_repository.get_ciudades()
    
    def add_city(self, city_name: str) -> dict:
        return self.city_repository.agregar_ciudad(city_name.lower())