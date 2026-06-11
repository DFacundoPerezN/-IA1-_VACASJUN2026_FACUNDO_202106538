from typing import List
from repositories.prolog_repo import PrologRepo
from repositories.sintoms_repo import SintomsRepo
from repositories.fails_repo import FailsRepo
from repositories.recommendations_repo import Recommendatios_Repo

class DoctorService:
    def __init__(self, prolog_repo: PrologRepo):
        self.prolog_repo = prolog_repo
        self.sintoms_repository = SintomsRepo(prolog_repo.prolog_file)
        self.fails_repository = FailsRepo(self.prolog_repo.prolog_file)
        self.recom_repository = Recommendatios_Repo(self.prolog_repo.prolog_file)

    def get_sintomas(self) -> List[str]:
        return self.sintoms_repository.get_sintomas()
    
    def get_falla_by_sintomas(self, listaSintomas: List) -> dict:
        return self.fails_repository.get_falla_por_sintomas(listaSintomas)
    
    def get_all_fallas(self) -> List[str]:
        return self.fails_repository.get_fallas()
    
    def get_recomendaciones_by_falla(self, falla: str) :
        return self.recom_repository.get_recomendaciones_por_falla(falla.lower())
    
    def get_recomendaciones_by_sintomas(self, listaSintomas: List) :
        return self.recom_repository.get_recomendaciones_por_sintomas(listaSintomas)
    
    def get_all_recomendaciones(self) -> List[str]:
        return self.recom_repository.get_recomendaciones()

    def add_sintoma(self, sintoma: str) -> dict:
        sintoma = sintoma.replace(" ","_")
        return self.sintoms_repository.add_sintoma(sintoma.lower())
    
    def add_falla(self, falla: str) -> dict:
        falla = falla.replace(" ","_")
        return self.fails_repository.add_falla(falla.lower())
    
    def add_recomendacion(self, recomendacion: str) -> dict:
        recomendacion = recomendacion.replace(" ","_")
        return self.recom_repository.add_recomendacion(recomendacion.lower())
    
    def conectar_falla_sintoma(self, falla: str, sintoma: str) -> dict:
        falla = falla.replace(" ","_").lower()
        sintoma = sintoma.replace(" ","_").lower()
        return self.sintoms_repository.falla_causada_por(falla, sintoma)
    
    def conectar_recomendacion_falla(self, recomendacion:str, falla:str) -> dict:
        falla = falla.replace(" ","_").lower()
        recomendacion = recomendacion.replace(" ","_")
        return self.fails_repository.tratamiento(recomendacion, falla)
    
    def delete_sintoma(self, sintoma:str) -> dict:
        sintoma = sintoma.replace(" ","_").lower()
        return self.sintoms_repository.delete_sintom(sintoma)
        
    def delete_falla(self, falla: str) -> dict:
        falla = falla.replace(" ","_")
        return self.fails_repository.delete_fail(falla)
    
    def delete_recomendacion(self, recomendacion: str) -> dict:
        recomendacion = recomendacion.replace(" ","_")
        return self.recom_repository.delete_recomendacion(recomendacion)