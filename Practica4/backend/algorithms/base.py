#Interfaz común para los algoritmos de búsqueda (Patrón Strategy).

from abc import ABC, abstractmethod
from models.maze import Maze
from models.search_result import SearchResult


class SearchAlgorithm(ABC):
    name: str = "abstract"

    @abstractmethod
    def search(self, maze: Maze) -> SearchResult:
        #Ejecuta el algoritmo de búsqueda sobre el laberinto dado.

        #SearchResult con la ruta encontrada (si existe), los nodos
        #    explorados y métricas del proceso de búsqueda.

        raise NotImplementedError