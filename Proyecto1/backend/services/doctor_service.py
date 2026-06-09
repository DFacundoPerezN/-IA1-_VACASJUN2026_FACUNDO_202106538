from typing import List
from repositories.prolog_repo import PrologRepo
from repositories.sintoms_repo import SintomsRepo

class DoctorService:
    def __init__(self, prolog_repo: PrologRepo):
        self.prolog_repo = prolog_repo
        self.sintoms_repository = SintomsRepo(prolog_repo.prolog_file)

    def get_sintomas(self) -> List[str]:
        return self.sintoms_repository.get_sintomas()