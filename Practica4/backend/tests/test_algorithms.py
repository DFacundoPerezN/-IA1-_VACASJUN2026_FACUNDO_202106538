#Tests unitarios para los algoritmos BFS y DFS, y para el modelo Maze.

#Ejecutar con: pytest

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest

from algorithms.bfs import BFSAlgorithm
from algorithms.dfs import DFSAlgorithm
from algorithms.astar import AStarAlgorithm
from models.maze import Maze, InvalidMazeError


def simple_maze():
    # 3x3 sin obstáculos
    return Maze(rows=3, cols=3, obstacles=[], start=(0, 0), goal=(2, 2))


def blocked_maze():
    # Laberinto donde el destino queda completamente aislado
    return Maze(
        rows=3, cols=3,
        obstacles=[(0, 1), (1, 0), (1, 1)],
        start=(0, 0), goal=(2, 2),
    )

 
def maze_with_detour():
    """
    Laberinto 5x5 con una pared vertical que obliga a rodear.
    El muro va de (0,2) a (3,2); hay un hueco en (4,2).
    S . # . .
    . . # . .
    . . # . .
    . . # . .
    . . . . G
    """
    obstacles = [(r, 2) for r in range(4)]
    return Maze(rows=5, cols=5, obstacles=obstacles, start=(0, 0), goal=(4, 4))


def test_bfs_finds_path_simple_maze():
    maze = simple_maze()
    result = BFSAlgorithm().search(maze)
    assert result.found is True
    assert result.path[0].to_tuple() == (0, 0)
    assert result.path[-1].to_tuple() == (2, 2)
    assert result.nodes_explored > 0


def test_dfs_finds_path_simple_maze():
    maze = simple_maze()
    result = DFSAlgorithm().search(maze)
    assert result.found is True
    assert result.path[0].to_tuple() == (0, 0)
    assert result.path[-1].to_tuple() == (2, 2)


def test_bfs_returns_shortest_path():
    # En un laberinto sin obstáculos 3x3, la ruta más corta de (0,0) a (2,2)
    # tiene longitud 5 (4 movimientos + celda inicial).
    maze = simple_maze()
    result = BFSAlgorithm().search(maze)
    assert len(result.path) == 5


def test_algorithms_fail_when_goal_unreachable():
    maze = blocked_maze()
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
    #Cada paso de la ruta debe ser un vecino válido del anterior.#
    maze = simple_maze()
    result = BFSAlgorithm().search(maze)
    for i in range(len(result.path) - 1):
        a, b = result.path[i], result.path[i + 1]
        dist = abs(a.row - b.row) + abs(a.col - b.col)
        assert dist == 1  # movimiento ortogonal de una sola celda

# Probando A*        
def test_astar_finds_path():
    r = AStarAlgorithm().search(simple_maze())
    assert r.found is True
    assert r.path[0].to_tuple() == (0, 0)
    assert r.path[-1].to_tuple() == (2, 2)
 
def test_astar_shortest_path():
    # A* garantiza ruta óptima, igual que BFS en costos uniformes
    r = AStarAlgorithm().search(simple_maze())
    assert len(r.path) == 5
 
def test_astar_blocked():
    r = AStarAlgorithm().search(blocked_maze())
    assert r.found is False
    assert r.path == []
 
def test_astar_same_length_as_bfs():
    """A* y BFS deben encontrar rutas de igual longitud (ambas óptimas)."""
    maze = maze_with_detour()
    r_astar = AStarAlgorithm().search(maze)
    r_bfs   = BFSAlgorithm().search(maze)
    assert r_astar.found is True
    assert len(r_astar.path) == len(r_bfs.path)
 
def test_astar_explores_fewer_nodes_than_bfs():
    """
    En laberintos con dirección clara, A* debe explorar menos nodos que BFS
    porque la heurística guía la búsqueda hacia el destino.
    """
    maze = maze_with_detour()
    r_astar = AStarAlgorithm().search(maze)
    r_bfs   = BFSAlgorithm().search(maze)
    assert r_astar.nodes_explored < r_bfs.nodes_explored

# python -m pytest tests/ -v 2>&1