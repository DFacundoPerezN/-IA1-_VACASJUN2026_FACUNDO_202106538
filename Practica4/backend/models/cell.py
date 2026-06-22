from dataclasses import dataclass

#@dataclass(frozen=True)
class Cell:
    """
    Representa una coordenada (fila, columna).

    Es inmutable (frozen=True) y hashable, lo cual permite usarla
    directamente como clave en sets/dicts (fundamental para BFS/DFS,
    donde necesitamos marcar celdas como "visitadas" de forma eficiente).
    """
    row: int
    col: int

    def __iter__(self):
        # Permite hacer: row, col = cell
        yield self.row
        yield self.col

    def to_tuple(self) -> tuple[int, int]:
        return (self.row, self.col)

    def to_dict(self) -> dict:
        return {"row": self.row, "col": self.col}

    def __repr__(self) -> str:
        return f"({self.row}, {self.col})"