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
def run_search(payload: SearchRequest):
    #Ejecuta un único algoritmo (BFS o DFS) sobre el laberinto enviado y devuelve la ruta encontrada, nodos explorados y tiempo de ejecución.
    try:
        result = service.run_search(
            algorithm_name=payload.algorithm,
            rows=payload.rows,
            cols=payload.cols,
            obstacles=_positions_to_tuples(payload.obstacles),
            start=(payload.start.row, payload.start.col),
            goal=(payload.goal.row, payload.goal.col),
        )
    except InvalidMazeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return result.to_dict()


@router.post("/compare",summary="Compara algoritmos")
def compare_algorithms(payload: CompareRequest):
    #Ejecuta BFS y DFS sobre el mismo laberinto y devuelve ambos resultados, útil para comparar desempeño en la interfaz web.
    try:
        results = service.run_comparison(
            rows=payload.rows,
            cols=payload.cols,
            obstacles=_positions_to_tuples(payload.obstacles),
            start=(payload.start.row, payload.start.col),
            goal=(payload.goal.row, payload.goal.col),
        )
    except InvalidMazeError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {name: result.to_dict() for name, result in results.items()}