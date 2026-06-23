from dataclasses import dataclass

#@dataclass(frozen=True)
class Cell:
    """
    Representa una coordenada (fila, columna).
    """
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def __eq__(self, other):
        return isinstance(other, Cell) and self.row == other.row and self.col == other.col

    def __hash__(self):
        return hash((self.row, self.col))

    def to_tuple(self) -> tuple[int, int]:
        return (self.row, self.col)

    def to_dict(self) -> dict:
        return {"row": self.row, "col": self.col}

    def __repr__(self) -> str:
        return f"({self.row}, {self.col})"