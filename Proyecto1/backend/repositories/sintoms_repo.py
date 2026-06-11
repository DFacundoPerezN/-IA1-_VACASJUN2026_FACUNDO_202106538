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
        
    def falla_causada_por(self, falla, sintoma):
        sintoma_atom = self._to_prolog_atom(sintoma)
        falla_atom = self._to_prolog_atom(falla)

        # Verificar que existan
        if self.query_one(f"once(sintoma({sintoma_atom})).") is None:
            return {"error": "Sintoma no existe"}
        
        if self.query_one(f"once(falla({falla_atom})).") is None:
            return {"error": "Falla no existe"}
        
        contenido = self.prolog_file.read_text(encoding="utf-8").splitlines()

        actualizado = False
        nueva_lineas=[]

        #caso 1 ya existe linea "falla_causada_por("
        for linea in contenido:
            s = linea.strip()

            # detecta correctamente la falla y ayuda a evitar el bug
            if s.startswith(f"falla_causada_por({falla_atom}"):
                # escribe solo una vez el nuevo falla_causada_por
                if not actualizado:
                    #verificamos no repetir sintomas
                    if sintoma in s:
                        return {"error": f"El sitoma {sintoma} ya esta relacionado con la falla"}
                    #dividimos en dos usando el nombre de la falla
                    partes = s.split(falla_atom)
                    partes[1] = partes[1].replace("]", f", {sintoma_atom}]")
                    linea = f"{partes[0]}{falla_atom}{partes[1]}"
                    #print("nueva linea: "+ linea)
                    actualizado = True

            nueva_lineas.append(linea)

        # Si no tenía conexion antes
        if not actualizado:
            nueva_linea =  f"falla_causada_por({falla_atom}, [{sintoma_atom}])."
            nueva_lineas.append(nueva_linea)

        #Sobreescribir el archivo
        self.prolog_file.write_text("\n".join(nueva_lineas), encoding="utf-8")

        #recargar prolog
        self._consult_file()

        return{
            "mensaje": "Relación falla sintoma actualizada", 
            "falla": falla_atom, 
            "sintoma": sintoma_atom
            }
    
    def delete_sintom(self, sintoma)->dict:
        sintoma_atom = self._to_prolog_atom(sintoma)

        if self.query_one(f"once(sintoma({sintoma_atom})).") is None:
            return {"error": "Sintoma no existe"}
        
        
        lineas = self.prolog_file.read_text(encoding="utf-8").splitlines()

        sintoma_linea = f"sintoma({sintoma_atom})."
        nuevas_lineas = []

        for linea in lineas:
            l = linea.strip()

            if l == sintoma_linea:
                continue

            if l.startswith("falla_causada_por("):
                if sintoma_atom in l:
                    if ',' in l:    
                        l = l.replace(f", {sintoma_atom}","")
                        l = l.replace(f"[{sintoma_atom}, ","[")
                    elif f"[{sintoma_atom}]" in l:
                        continue

            nuevas_lineas.append(linea)               
            
        self.prolog_file.write_text("\n".join(nuevas_lineas), encoding="utf-8")
        self._consult_file()

        return{
            "mensaje": "Sintoma borrado", 
            "sintoma": sintoma_atom
        }


