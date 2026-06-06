from pyswip import Prolog
from pathlib import Path
import re
from typing import List

class PrologRepo:
    def __init__(self, prolog_file):
        self.prolog_file = Path(prolog_file).resolve()
        self.aux_file = Path("c_aux.pl").resolve()
        self.prolog = Prolog()
        self._consult_file()

    def _consult_file(self):
        path_str = self.prolog_file.as_posix()
        list(self.prolog.query(f"unload_file('{path_str}')")) # Asegura la recarga del disco
        list(self.prolog.query(f"consult('{path_str}')"))

        if self.aux_file.exists():
            aux_str = self.aux_file.as_posix()
            list(self.prolog.query(f"unload_file('{aux_str}')")) # Asegura la recarga del disco
            list(self.prolog.query(f"consult('{aux_str}')"))

    def query_one(self, query_str: str):
        return next(self.prolog.query(query_str), None)

    def query(self, query_str):
        return list(self.prolog.query(query_str))
    
    # Redefinir para atomizar datos
    _safe_atom_re = re.compile(r'^[a-z][a-zA-Z0-9_]*$')

    
    def _to_prolog_atom(self, s:str) -> str:
        s = s.strip()
        if self._safe_atom_re.match(s): #juan Juan
            return s
        
        s_escaped = s.replace("'", "''") # Juan -> 'Juan'
        return f"'{s_escaped}'"

    def existe_ciudad(self, ciudad:str) -> bool:
        ciudad_atom = self._to_prolog_atom(ciudad)
        query_str = f"ciudad({ciudad_atom})"
        return bool(self.query_one(query_str))

    def get_ciudades(self) -> List[str]:
        sol = self.query_one("get_ciudades(Lista)")
        if not sol:
            return []
        return [str(ciudad) for ciudad in sol['Lista']]
    
    # POST
    def agregar_ciudad(self, ciudad:str) -> bool:       
        
        if self.existe_ciudad(ciudad):
            print(f"La ciudad '{ciudad}' ya existe.")
            return {
                "success": False,
                "message": f"La ciudad '{ciudad}' ya existe.",
                "code": 400
            }

        ciudad_atom = self._to_prolog_atom(ciudad)
        try:
            # Agregar la nueva ciudad al archivo auxiliar, el otro es prolog_file
            with self.aux_file.open('a') as f:
                f.write(f"ciudad({ciudad_atom}).\n")

            self._consult_file()  # Recargar el archivo para que Prolog reconozca la nueva ciudad
            return {
                "success": True,
                "message": f"La ciudad '{ciudad}' fue agregada exitosamente.",
                "code": 201
            }
        except Exception as e:
            print(f"Error al agregar ciudad: {e}")
            return {
                "success": False,
                "message": f"Error al agregar ciudad '{ciudad}': {e}",
                "code": 500
            }