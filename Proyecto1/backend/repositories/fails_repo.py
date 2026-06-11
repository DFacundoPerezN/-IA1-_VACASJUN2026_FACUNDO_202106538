import repositories.prolog_repo as prolog_repo
from typing import List

class FailsRepo(prolog_repo.PrologRepo):
    def __init__(self, prolog_file):
        super().__init__(prolog_file)

    def get_fallas(self) -> List[str]:
        sol = self.query_one("get_fallas(Lista)")
        if not sol:
            return []
        return [str(falla) for falla in sol['Lista']]
    
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
        
    def tratamiento(self, recomendacion, falla):
        recom_atom = self._to_prolog_atom(recomendacion)
        falla_atom = self._to_prolog_atom(falla)

        # Verificar que existan
        if self.query_one(f"once(recomendacion({recom_atom})).") is None:
            return {"error": "Recomendacion no existe"}
        
        if self.query_one(f"once(falla({falla_atom})).") is None:
            return {"error": "Falla no existe"}
        
        contenido = self.prolog_file.read_text(encoding="utf-8").splitlines()

        actualizado = False
        nueva_lineas=[]

        #caso 1 ya existe linea "tratamiento("
        for linea in contenido:
            s = linea.strip()

            # detecta correctamente la falla y ayuda a evitar el bug
            if s.startswith(f"tratamiento({falla_atom}"):
                # escribe solo una vez el nuevo falla_causada_por
                if not actualizado:
                    print("existe tratamiento")
                    #verificamos no repetir sintomas
                    if recom_atom in s:
                        return {"error": f"La recomendacion: {recom_atom} ya esta relacionada con la falla"}
                    #dividimos en dos usando el nombre de la falla
                    partes = s.split(falla_atom)
                    partes[1] = partes[1].replace("]", f", {recom_atom}]")
                    linea = f"{partes[0]}{falla_atom}{partes[1]}"
                    print("nueva linea: "+ linea)
                    actualizado = True

            nueva_lineas.append(linea)
            
        # Si no tenía conexion antes
        if not actualizado:
            nueva_linea =  f"tratamiento({falla_atom}, [{recom_atom}])."
            nueva_lineas.append(nueva_linea)

        #Sobreescribir el archivo
        self.prolog_file.write_text("\n".join(nueva_lineas), encoding="utf-8")
        #recargar prolog
        self._consult_file()

        return{
            "mensaje": "Relación falla recomendación actualizada", 
            "falla": falla_atom, 
            "recomendacion": recom_atom
            }
                
    def delete_fail(self, falla)->dict:
        falla_atom = self._to_prolog_atom(falla)

        if self.query_one(f"once(falla({falla_atom})).") is None:
            return {"error": "Falla no existe"}
        
        
        lineas = self.prolog_file.read_text(encoding="utf-8").splitlines()

        falla_linea = f"falla({falla_atom})."
        nuevas_lineas = []

        for linea in lineas:
            l = linea.strip()

            if l == falla_linea:
                continue

            if l.startswith(f"falla_causada_por({falla_atom}"):
                continue

            if l.startswith(f"tratamiento({falla_atom}"):
                continue

            nuevas_lineas.append(linea)               
            
        self.prolog_file.write_text("\n".join(nuevas_lineas), encoding="utf-8")
        self._consult_file()

        return{
            "mensaje": "Falla borrada", 
            "falla": falla_atom
        }

                