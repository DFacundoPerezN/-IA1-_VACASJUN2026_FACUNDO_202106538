#Algoritmo Breadth-First Search (BFS)

import time
from collections import deque

from app.algorithms.base import SearchAlgorithm
from app.domain.cell import Cell
from app.domain.maze import Maze
from app.domain.search_result import SearchResult


class BFSAlgorithm(SearchAlgorithm):
    name = "BFS"

    def search(self, maze: Maze) -> SearchResult:
        start_time = time.perf_counter()

        start = maze.start
        goal = maze.goal

        frontier: deque[Cell] = deque([start])
        came_from: dict[Cell, Cell | None] = {start: None}
        explored_order: list[Cell] = []

        found = False

        while frontier:
            current = frontier.popleft()  # FIFO -> característica clave de BFS
            explored_order.append(current)

            if current == goal:
                found = True
                break

            for neighbor in maze.neighbors(current):
                if neighbor not in came_from:
                    came_from[neighbor] = current
                    frontier.append(neighbor)

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
    def _reconstruct_path(came_from: dict[Cell, Cell | None], start: Cell, goal: Cell) -> list[Cell]:
        path = [goal]
        current = goal
        while current != start:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path