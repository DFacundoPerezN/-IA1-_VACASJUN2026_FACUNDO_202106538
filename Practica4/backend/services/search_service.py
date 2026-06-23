"""
Servicio de búsqueda (MazeSearchService)

Orquesta el caso de uso completo: construir el Maze a partir de
datos de entrada, seleccionar el algoritmo vía la Factory, ejecutarlo y devolver el resultado. Esta capa es la que usaría
también, por ejemplo, una CLI o tests, sin depender de FastAPI.
"""
from algorithms.factory import get_algorithm
from models.maze import Maze
from models.search_result import SearchResult


class MazeSearchService:
    def run_search(self, algorithm_name: str, rows: int, cols: int, obstacles: list[tuple[int, int]], start: tuple[int, int], goal: tuple[int, int]) -> SearchResult:

        maze = Maze(rows=rows, cols=cols, obstacles=obstacles, start=start, goal=goal)
        algorithm = get_algorithm(algorithm_name)
        return algorithm.search(maze)

    def run_comparison(self, rows: int, cols: int, obstacles: list[tuple[int, int]],start: tuple[int, int], goal: tuple[int, int] ) -> dict[str, SearchResult]:

        #Ejecuta BFS y DFS sobre el mismo laberinto para comparar resultados
        maze = Maze(rows=rows, cols=cols, obstacles=obstacles, start=start, goal=goal)
        results = {}
        for name in ("bfs", "dfs"):
            algorithm = get_algorithm(name)
            results[name] = algorithm.search(maze)
        return results