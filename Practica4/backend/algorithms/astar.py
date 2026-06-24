"""
Algoritmo A* (A-estrella)

Diferencias clave con BFS y DFS:
- BFS usa una cola FIFO  → explora por niveles, sin dirección
- DFS usa una pila LIFO  → va profundo sin dirección
- A*  usa una HEAP       → siempre explora la celda más prometedora primero

La "promesa" de una celda se mide con: f = g + h
"""
import heapq
import time

from algorithms.base import SearchAlgorithm
from algorithms.heuristicsA import manhattan
from models.cell import Cell
from models.maze import Maze
from models.search_result import SearchResult


class AStarAlgorithm(SearchAlgorithm):
    name = "A*"

    def search(self, maze: Maze) -> SearchResult:
        start_time = time.perf_counter()

        start = maze.start
        goal  = maze.goal

        # ------------------------------------------------------------------ #
        # PASO 1: Inicializar la open list (cola de prioridad / min-heap)
        #
        # Cada elemento de la heap es una tupla:  (f, celda)
        # Python ordena las tuplas por el primer elemento → siempre
        # extraemos la celda con menor f primero (min-heap).
        #
        # Estructura: open_list = [(f0, start), (f1, celda_a), ...]
        # ------------------------------------------------------------------ #
        h_start = manhattan(start, goal)
        open_list = [(h_start, start)]   # f = g + h = 0 + h_start

        # ------------------------------------------------------------------ #
        # PASO 2: Rastrear el costo g real de llegar a cada celda
        #
        # g_cost[celda] = cantidad de pasos desde el inicio hasta esa celda.
        # Comenzamos conociendo solo el costo del inicio: 0.
        # ------------------------------------------------------------------ #
        g_cost: dict[Cell, int] = {start: 0}

        # ------------------------------------------------------------------ #
        # PASO 3: Rastrear de dónde venimos (para reconstruir la ruta)
        # ------------------------------------------------------------------ #
        came_from: dict[Cell, Cell | None] = {start: None}

        # Para registrar el orden de exploración (métricas de la UI)
        explored_order: list[Cell] = []
        visited: set[Cell] = set()

        found = False

        # ------------------------------------------------------------------ #
        # PASO 4: Bucle principal
        # ------------------------------------------------------------------ #
        while open_list:

            # Extraer la celda con menor f (la más prometedora)
            _, current = heapq.heappop(open_list)

            # Saltar si ya fue procesada (puede haber duplicados en la heap)
            if current in visited:
                continue
            visited.add(current)
            explored_order.append(current)

            # ¿Llegamos al destino?
            if current == goal:
                found = True
                break

            # -------------------------------------------------------------- #
            # PASO 5: Expandir vecinos
            # -------------------------------------------------------------- #
            for neighbor in maze.neighbors(current):
                if neighbor in visited:
                    continue

                # El costo g del vecino es el costo de llegar al actual + 1
                tentative_g = g_cost[current] + 1

                # Solo actualizamos si encontramos un camino MEJOR que el conocido
                if tentative_g < g_cost.get(neighbor, float("inf")):
                    g_cost[neighbor]    = tentative_g
                    came_from[neighbor] = current

                    # Calcular f = g + h y agregar a la heap
                    h = manhattan(neighbor, goal)
                    f = tentative_g + h
                    heapq.heappush(open_list, (f, neighbor))

        path = self._reconstruct_path(came_from, start, goal) if found else []
        elapsed_ms = (time.perf_counter() - start_time) * 1000

        return SearchResult(
            algorithm=self.name,
            found=found,
            path=path,
            explored_order=explored_order,
            nodes_explored=len(explored_order),
            execution_time_ms=elapsed_ms,
        )

    @staticmethod
    def _reconstruct_path(
        came_from: dict[Cell, Cell | None], start: Cell, goal: Cell
    ) -> list[Cell]:
        path = [goal]
        current = goal
        while current != start:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path