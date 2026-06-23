from fastapi import APIRouter, HTTPException

from algorithms.factory import available_algorithms
from api.schemas import CompareRequest, SearchRequest
from models.maze import InvalidMazeError
from services.search_service import MazeSearchService

router = APIRouter(prefix="", tags=["maze"])
service = MazeSearchService()


def _positions_to_tuples(positions) -> list[tuple[int, int]]:
    return [(p.row, p.col) for p in positions]


@router.get("/algorithms")
def list_algorithms():
    #Devuelve los algoritmos de búsqueda disponibles.
    return {"algorithms": available_algorithms()}


@router.post("/search")
def run_search(data: SearchRequest):
    #Ejecuta un único algoritmo (BFS o DFS) sobre el laberinto enviado y devuelve la ruta encontrada, nodos explorados y tiempo de ejecución.
    try:
        result = service.run_search(
            algorithm_name=data.algorithm,
            rows=data.rows,
            cols=data.cols,
            start=(data.start.row, data.start.col),
            goal=(data.goal.row, data.goal.col),
            obstacles=_positions_to_tuples(data.obstacles),
        )
    except InvalidMazeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return result.to_dict()


@router.post("/compare",summary="Compara algoritmos")
def compare_algorithms(data: CompareRequest):
    #Ejecuta BFS y DFS sobre el mismo laberinto y devuelve ambos resultados, útil para comparar desempeño en la interfaz web.
    try:
        results = service.run_comparison(
            rows=data.rows,
            cols=data.cols,
            obstacles=_positions_to_tuples(data.obstacles),
            start=(data.start.row, data.start.col),
            goal=(data.goal.row, data.goal.col),
        )
        """
        [f][ ][ ]
        [+][ ][+]
        [ ][ ][s]
        rows= 3,
        cols = 3,
        start = {row = 2, col =2},
        goal = {row = 0, col = 0},
        obstacels = [{row = 1, col =0},{row = 1, col =2}]
        """
    except InvalidMazeError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {name: result.to_dict() for name, result in results.items()}