from typing import List
from repositories.prolog_repo import PrologRepo
from repositories.sintoms_repo import SintomsRepo
from repositories.fails_repo import FailsRepo
from repositories.recommendations_repo import Recommendatios_Repo
from telegram.bot import TelegramBot 

class DoctorService:
    def __init__(self, prolog_repo: PrologRepo):
        self.prolog_repo = prolog_repo
        self.sintoms_repository = SintomsRepo(prolog_repo.prolog_file)
        self.fails_repository = FailsRepo(self.prolog_repo.prolog_file)
        self.recom_repository = Recommendatios_Repo(self.prolog_repo.prolog_file)
        self.bot = TelegramBot()

    def get_sintomas(self) -> List[str]:
        return self.sintoms_repository.get_sintomas()
    
    def get_falla_by_sintomas(self, listaSintomas: List, notificar= True) -> dict:
        response = self.fails_repository.get_falla_por_sintomas(listaSintomas)
        if (notificar):
            if (response["falla"] is not None ) and (response["falla"] != []):
                self.bot.enviar_falla(listaSintomas, response["falla"])
        return response
    
    def get_all_fallas(self) -> List[str]:
        return self.fails_repository.get_fallas()
    
    def get_recomendaciones_by_falla(self, falla: str) :
        return self.recom_repository.get_recomendaciones_por_falla(falla.lower())
    
    def get_recomendaciones_by_sintomas(self, listaSintomas: List, notificar = True) :
        response = self.recom_repository.get_recomendaciones_por_sintomas(listaSintomas)        
        if (notificar):
            if (response["recommendations"] is not None ) and (response["recommendations"] != []):
                self.bot.enviar_recomendaciones(listaSintomas, response["recommendations"])
        return response
    
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
        falla = falla.replace(" ","_").lower()
        return self.fails_repository.delete_fail(falla)
    
    def delete_recomendacion(self, recomendacion: str) -> dict:
        recomendacion = recomendacion.replace(" ","_").lower()
        return self.recom_repository.delete_recomendacion(recomendacion)
    
    def update_sintoma(self, old: str, new:str) -> dict:
        old = old.replace(" ","_").lower()
        new = new.replace(" ","_").lower()
        return self.sintoms_repository.update_sintom(old, new)
    
    def update_falla(self, old: str, new:str) -> dict:
        old = old.replace(" ","_").lower()
        new = new.replace(" ","_").lower()
        return self.fails_repository.update_fail(old, new)
    
    def update_recomendacion(self, old: str, new:str) -> dict:
        old = old.replace(" ","_").lower()
        new = new.replace(" ","_").lower()
        return self.recom_repository.update_recommendation(old, new)
    
    def update_chat_id(self, chat_id: str) :
        self.bot.cambiar_chat(chat_id)
        return{"message":"se cambio correcatemente el id del chat"}