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
    
    def get_falla(self, listaSintomas: List) -> dict:
        return self.fails_repository.get_falla_por_sintomas(listaSintomas)
    
    def get_recomendaciones_by_falla(self, falla: str) :
        return self.recom_repository.get_recomendaciones_por_falla(falla)
    
    def get_recomendaciones_by_sintomas(self, listaSintomas: List) :
        return self.recom_repository.get_recomendaciones_por_sintomas(listaSintomas)