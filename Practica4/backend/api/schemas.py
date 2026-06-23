from pydantic import BaseModel, Field


class Position(BaseModel):
    row: int
    col: int


class SearchRequest(BaseModel):
    rows: int = Field(..., gt=0, description="Número de filas del laberinto")
    cols: int = Field(..., gt=0, description="Número de columnas del laberinto")
    obstacles: list[Position] = Field(default_factory=list)
    start: Position
    goal: Position
    algorithm: str = Field(..., description="Algoritmo a ejecutar: 'bfs' o 'dfs'")

    class Config:
        json_schema_extra = {
            "example": {
                "rows": 5,
                "cols": 5,
                "obstacles": [{"row": 1, "col": 1}, {"row": 1, "col": 2}],
                "start": {"row": 0, "col": 0},
                "goal": {"row": 4, "col": 4},
                "algorithm": "bfs",
            }
        }


class CompareRequest(BaseModel):
    rows: int = Field(..., gt=0)
    cols: int = Field(..., gt=0)
    obstacles: list[Position] = Field(default_factory=list)
    start: Position
    goal: Position