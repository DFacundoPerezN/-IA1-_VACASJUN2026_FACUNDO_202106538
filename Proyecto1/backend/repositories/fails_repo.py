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

    def add_falla(self, falla):
        falla_atom = self._to_prolog_atom(falla)
        try:
            # Agregando falla al prolog_file
            with self.prolog_file.open('a') as f:
                f.write(f"falla({falla_atom}).\n")

            self._consult_file()  # Recargar el archivo para que Prolog reconozca la nueva ciudad
            return {
                "success": True,
                "message": f"La falla '{falla_atom}' fue agregada con exitos.",
                "code": 201
            }
        except Exception as e:
            print(f"Error al agregar falla: {e}")
            return {
                "success": False,
                "message": f"Error al agregar la falla '{falla_atom}': {e}",
                "code": 500
            }
                