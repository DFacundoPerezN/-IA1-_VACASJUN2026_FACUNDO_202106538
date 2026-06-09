import repositories.prolog_repo as prolog_repo

class Recommendatios_Repo(prolog_repo.PrologRepo):

    def __init__(self, prolog_file):
        super().__init__(prolog_file)

    def get_recomendaciones_por_sintomas(self, lista):
        sintomas="["
        for i in lista:
            sintomas += str(i) + ","
        sintomas = sintomas[:-1] + "]"

        sol = self.query_one(f"obtener_recomendaciones({sintomas}, Recomendaciones).")

        if not sol:
            return {    
                "code": 201,
                "falla": None,
                "message": "No se encontró una falla designada a esos sintomas"
            }

        return {
            "code": 201,
            "recommendations": [str(c) for c in sol['Recomendaciones']]
        }

    def get_recomendaciones_por_falla(self, falla: str):
        falla = self._to_prolog_atom(falla)

        sol = self.query_one(f" tratamiento({falla}, Recomendaciones)")

        if not sol:
            return {    
                "code": 201,
                "falla": None,
                "message": "No se encontró una falla designada a esos sintomas"
            }

        return {
            "code": 201,
            "recommendations": [str(c) for c in sol['Recomendaciones']]
        }