from __future__ import annotations
from models.cell import Cell


class InvalidMazeError(Exception):
    #Se lanza cuando la configuración del laberinto es inválida.
    pass


class Maze:
    """
    Cuadrícula bidimensional que representa el laberinto.

    - 0 = celda libre (transitable)
    - 1 = obstáculo (bloquea el paso)
    """

    def __init__(self, rows: int,cols: int, obstacles: list[tuple[int, int]],
        start: tuple[int, int],goal: tuple[int, int]):

        if rows <= 0 or cols <= 0:
            raise InvalidMazeError("Las dimensiones del laberinto deben ser positivas")

        self.rows = rows
        self.cols = cols
        self.start = Cell(*start)
        self.goal = Cell(*goal)
        self.obstacles: set[Cell] = {Cell(r, c) for r, c in obstacles}

        self._validate()

    def _validate(self) -> None:
        if not self.in_bounds(self.start):
            raise InvalidMazeError(f"La posición de inicio {self.start} está fuera del laberinto")
        if not self.in_bounds(self.goal):
            raise InvalidMazeError(f"La posición destino {self.goal} está fuera del laberinto")
        if self.start in self.obstacles:
            raise InvalidMazeError("La posición de inicio coincide con un obstáculo")
        if self.goal in self.obstacles:
            raise InvalidMazeError("La posición destino coincide con un obstáculo")
        for obs in self.obstacles:
            if not self.in_bounds(obs):
                raise InvalidMazeError(f"Obstáculo {obs} está fuera del laberinto")

    def in_bounds(self, cell: Cell) -> bool:
        return 0 <= cell.row < self.rows and 0 <= cell.col < self.cols

    def is_walkable(self, cell: Cell) -> bool:
        #Una celda es transitable si está dentro del tablero y no es obstáculo.
        return self.in_bounds(cell) and cell not in self.obstacles

    def neighbors(self, cell: Cell) -> list[Cell]:
        #Devuelve las celdas vecinas transitables 
        candidates = [
            Cell(cell.row - 1, cell.col),  # arriba
            Cell(cell.row + 1, cell.col),  # abajo
            Cell(cell.row, cell.col - 1),  # izquierda
            Cell(cell.row, cell.col + 1),  # derecha
        ]
        return [c for c in candidates if self.is_walkable(c)]

    def to_dict(self) -> dict:
        return {
            "rows": self.rows,
            "cols": self.cols,
            "start": self.start.to_dict(),
            "goal": self.goal.to_dict(),
            "obstacles": [o.to_dict() for o in self.obstacles],
        }