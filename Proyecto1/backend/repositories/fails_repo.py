import repositories.prolog_repo as prolog_repo

class FailsRepo(prolog_repo.PrologRepo):
    def __init__(self, prolog_file):
        super().__init__(prolog_file)

    def get_falla_por_sintomas(self, lista):
        sintomas="["
        for i in lista:
            sintomas += str(i) + ","
        sintomas = sintomas[:-1] + "]"
        sol = self.query_one(f"diagnosticar({sintomas}, Falla).")

        if not sol:
            return {    
                "code": 201,
                "falla": None,
                "message": "No se encontró una falla designada a esos sintomas"
                }
        
        return {            
            "code": 201,
            "falla": sol["Falla"]
        }