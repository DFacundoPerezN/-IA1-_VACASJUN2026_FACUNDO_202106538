#Algoritmo Depth-First Search (DFS)

import time

from algorithms.base import SearchAlgorithm
from models.cell import Cell
from models.maze import Maze
from models.search_result import SearchResult


class DFSAlgorithm(SearchAlgorithm):
    name = "DFS"

    def search(self, maze: Maze) -> SearchResult:
        start_time = time.perf_counter()

        start = maze.start
        goal = maze.goal

        stack: list[Cell] = [start]
        came_from: dict[Cell, Cell | None] = {start: None}
        visited: set[Cell] = set()
        explored_order: list[Cell] = []

        found = False

        while stack:
            current = stack.pop()  # LIFO -> característica clave de DFS

            if current in visited:
                continue
            visited.add(current)
            explored_order.append(current)

            if current == goal:
                found = True
                break

            for neighbor in maze.neighbors(current):
                if neighbor not in visited and neighbor not in came_from:
                    came_from[neighbor] = current
                    stack.append(neighbor)

        path = self._reconstruct_models(came_from, start, goal) if found else []
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
    def _reconstruct_models(
        came_from: dict[Cell, Cell | None], start: Cell, goal: Cell
    ) -> list[Cell]:
        models = [goal]
        current = goal
        while current != start:
            current = came_from[current]
            models.append(current)
        models.reverse()
        return models