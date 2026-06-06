from pyswip import Prolog
from pathlib import Path
import re
from typing import List

class PrologRepo:
    def __init__(self, prolog_file):
        self.prolog_file = Path(prolog_file).resolve()
        self.prolog = Prolog()
        self._consult_file()

    def _consult_file(self):
        path_str = self.prolog_file.as_posix()
        list(self.prolog.query(f"consult('{path_str}')"))

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
    
    def obtener_ciudad(self, nombre_ciudad):
        nombre_ciudad_atom = self._to_prolog_atom(nombre_ciudad)
        query_str = f"ciudad({nombre_ciudad_atom}, Poblacion, Pais)"
        return self.query_one(query_str)
    
    def get_ciudades(self) -> List[str]:
        sol = self.query_one("get_ciudades(Lista)")
        if not sol:
            return []
        return [str(ciudad) for ciudad in sol['Lista']]