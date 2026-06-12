import repositories.prolog_repo as prolog_repo
from typing import List

class Recommendatios_Repo(prolog_repo.PrologRepo):

    def __init__(self, prolog_file):
        super().__init__(prolog_file)

    def get_recomendaciones(self) -> List[str]:
        sol = self.query_one("get_recomendaciones(Lista).")
        if not sol:
            return []
        return [str(falla) for falla in sol['Lista']]

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
                "recommendations":[],
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
                "recommendations":[],
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
                f.write(f"\nrecomendacion({recom_atom}).\n")

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
        
    def delete_recomendacion(self, recomendacion)->dict:
        recom_atom = self._to_prolog_atom(recomendacion)

        if self.query_one(f"once(recomendacion({recom_atom})).") is None:
            return {"error": "Recomendacion no existe"}
                
        lineas = self.prolog_file.read_text(encoding="utf-8").splitlines()

        recom_linea = f"recomendacion({recom_atom})."
        nuevas_lineas = []

        for linea in lineas:
            l = linea.strip()

            if l == recom_linea:
                continue

            if l.startswith("tratamiento("):
                if recom_atom in l:
                    print("linea con tratamiento y recomendacion: "+l)
                    if "," in l:    
                        l = l.replace(f", {recom_atom}","")
                        linea = l.replace(f"[{recom_atom}, ","[")
                    elif f"[{recom_atom}]" in l:
                        continue

            nuevas_lineas.append(linea)               
            
        self.prolog_file.write_text("\n".join(nuevas_lineas), encoding="utf-8")
        self._consult_file()

        return{
            "mensaje": "Recomendacion borrada", 
            "recomendacion": recom_atom
        }
    
    def update_recommendation(self, old_name, new_name):
        old_atom = self._to_prolog_atom(old_name)
        new_atom = self._to_prolog_atom(new_name)
        
        if self.query_one(f"once(recomendacion({old_atom})).") is None:
            return {"error": f"Recomendacion {old_atom} no existe"}

        # if self.query_one(f"once(recomendacion({new_atom})).") is not None:
        #     return {"error": f"Recomendacion con el nuevo nombre {new_atom} ya existe"}

        content = self.prolog_file.read_text(encoding="utf-8")
        content = content.replace(old_atom, new_atom)

        self.prolog_file.write_text(content, encoding="utf-8")
        self._consult_file()

        return{
            "mensaje": "Recomendacion editada", 
            "nombre_viejo": old_atom,
            "nombre_nuevo": new_atom
        }