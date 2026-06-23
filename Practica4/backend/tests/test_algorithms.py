"""
Tests unitarios para los algoritmos BFS y DFS, y para el modelo Maze.

Ejecutar con: pytest
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest

from algorithms.bfs import BFSAlgorithm
from algorithms.dfs import DFSAlgorithm
from models.maze import Maze, InvalidMazeError


def make_simple_maze():
    # 3x3 sin obstáculos
    return Maze(rows=3, cols=3, obstacles=[], start=(0, 0), goal=(2, 2))


def make_blocked_maze():
    # Laberinto donde el destino queda completamente aislado
    return Maze(
        rows=3, cols=3,
        obstacles=[(0, 1), (1, 0), (1, 1)],
        start=(0, 0), goal=(2, 2),
    )


def test_bfs_finds_path_simple_maze():
    maze = make_simple_maze()
    result = BFSAlgorithm().search(maze)
    assert result.found is True
    assert result.path[0].to_tuple() == (0, 0)
    assert result.path[-1].to_tuple() == (2, 2)
    assert result.nodes_explored > 0


def test_dfs_finds_path_simple_maze():
    maze = make_simple_maze()
    result = DFSAlgorithm().search(maze)
    assert result.found is True
    assert result.path[0].to_tuple() == (0, 0)
    assert result.path[-1].to_tuple() == (2, 2)


def test_bfs_returns_shortest_path():
    # En un laberinto sin obstáculos 3x3, la ruta más corta de (0,0) a (2,2)
    # tiene longitud 5 (4 movimientos + celda inicial).
    maze = make_simple_maze()
    result = BFSAlgorithm().search(maze)
    assert len(result.path) == 5


def test_algorithms_fail_when_goal_unreachable():
    maze = make_blocked_maze()
    bfs_result = BFSAlgorithm().search(maze)
    dfs_result = DFSAlgorithm().search(maze)
    assert bfs_result.found is False
    assert dfs_result.found is False
    assert bfs_result.path == []
    assert dfs_result.path == []


def test_maze_rejects_start_on_obstacle():
    with pytest.raises(InvalidMazeError):
        Maze(rows=3, cols=3, obstacles=[(0, 0)], start=(0, 0), goal=(2, 2))


def test_maze_rejects_out_of_bounds_goal():
    with pytest.raises(InvalidMazeError):
        Maze(rows=3, cols=3, obstacles=[], start=(0, 0), goal=(5, 5))


def test_path_is_contiguous():
    """Cada paso de la ruta debe ser un vecino válido del anterior."""
    maze = make_simple_maze()
    result = BFSAlgorithm().search(maze)
    for i in range(len(result.path) - 1):
        a, b = result.path[i], result.path[i + 1]
        dist = abs(a.row - b.row) + abs(a.col - b.col)
        assert dist == 1  # movimiento ortogonal de una sola celda