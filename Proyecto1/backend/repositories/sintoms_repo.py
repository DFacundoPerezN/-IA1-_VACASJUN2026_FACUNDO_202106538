import repositories.prolog_repo as prolog_repo

class SintomsRepo(prolog_repo.PrologRepo):
    def __init__(self, prolog_file):
        super().__init__(prolog_file)

    def get_sintomas(self):
        sols = self.query("sintoma(X).")
        return [str(sol['X']) for sol in sols]
    
    def add_sintoma(self, sintoma):

        sintoma_atom = self._to_prolog_atom(sintoma)
        try:
            # Agregar nuevo sintoma al prolog_file
            with self.prolog_file.open('a') as f:
                f.write(f"sintoma({sintoma_atom}).\n")

            self._consult_file()  # Recargar el archivo para que Prolog reconozca la nueva ciudad
            return {
                "success": True,
                "message": f"El sintoma '{sintoma_atom}' fue agregado con exitoso.",
                "code": 201
            }
        except Exception as e:
            print(f"Error al agregar sintoma: {e}")
            return {
                "success": False,
                "message": f"Error al agregar el sintoma '{sintoma_atom}': {e}",
                "code": 500
            }
                