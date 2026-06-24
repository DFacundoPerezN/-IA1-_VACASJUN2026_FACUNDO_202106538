"""
Factory de algoritmos.

Centraliza la creación de instancias de SearchAlgorithm a partir
de un identificador en texto (ej. "bfs", "dfs"). Esto desacopla
a la capa de servicios/API de las clases concretas de cada algoritmo,
y facilita agregar nuevos algoritmos en el futuro (Open/Closed Principle).
"""
from algorithms.base import SearchAlgorithm
from algorithms.bfs import BFSAlgorithm
from algorithms.dfs import DFSAlgorithm
from algorithms.astar import AStarAlgorithm 

class UnknownAlgorithmError(Exception):
    pass

_ALGORITHMS: dict[str, type[SearchAlgorithm]] = {
    "bfs": BFSAlgorithm,
    "dfs": DFSAlgorithm,
    "astar": AStarAlgorithm
}


def get_algorithm(name: str) -> SearchAlgorithm:
    """Devuelve una instancia del algoritmo solicitado."""
    key = name.strip().lower()
    if key not in _ALGORITHMS:
        valid = ", ".join(_ALGORITHMS.keys())
        raise UnknownAlgorithmError(
            f"Algoritmo '{name}' no soportado. Opciones válidas: {valid}"
        )
    return _ALGORITHMS[key]()


def available_algorithms() -> list[str]:
    return list(_ALGORITHMS.keys())