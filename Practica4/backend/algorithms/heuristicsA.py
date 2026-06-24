"""
Heurística para A*: Distancia Manhattan

La distancia Manhattan cuenta cuántos pasos ortogonales (sin diagonales)
hay entre dos celdas. Es la heurística correcta para cuadrículas con
movimiento en 4 direcciones porque:

1. Nunca sobreestima el costo real (es "admisible")
   → Esto garantiza que A* siempre encuentre la ruta más corta.

2. Es rápida de calcular: solo dos restas y dos valores absolutos.

Ejemplo visual:
    S . . .
    . . . .
    . . . G

    Manhattan(S, G) = |0-2| + |0-3| = 2 + 3 = 5
    (mínimo 5 pasos para llegar, sin importar los muros)
"""
from models.cell import Cell


def manhattan(a: Cell, b: Cell) -> int:
    return abs(a.row - b.row) + abs(a.col - b.col)