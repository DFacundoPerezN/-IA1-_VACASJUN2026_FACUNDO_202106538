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
    
    def add_recomendacion(self, recomendacion:str ):
        recom_atom = self._to_prolog_atom(recomendacion)
        try:
            # Agregar nuevo recomendacion al prolog_file
            with self.prolog_file.open('a') as f:
                f.write(f"recomendacion({recom_atom}).\n")

            self._consult_file()  # Recargar el archivo para que Prolog reconozca la nueva ciudad
            return {
                "success": True,
                "message": f"La recomendacion '{recom_atom}' fue agregada con exito.",
                "code": 201
            }
        except Exception as e:
            print(f"Error al agregar la recomendacion: {e}")
            return {
                "success": False,
                "message": f"Error al agregar la recomendacion '{recom_atom}': {e}",
                "code": 500
            }