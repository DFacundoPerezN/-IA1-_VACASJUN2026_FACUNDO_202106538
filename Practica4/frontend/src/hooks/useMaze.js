import { useState, useCallback } from "react";
import { runSearch } from "../api/mazeApi";

const ROWS = 15;
const COLS = 20;

export const CELL_TYPES = {
  EMPTY: "empty",
  WALL: "wall",
  START: "start",
  GOAL: "goal",
  EXPLORED: "explored",
  PATH: "path",
};

const buildEmptyGrid = () =>
  Array.from({ length: ROWS }, () => Array(COLS).fill(CELL_TYPES.EMPTY));

export function useMaze() {
  const [grid, setGrid] = useState(buildEmptyGrid);
  const [mode, setMode] = useState("wall"); // "wall" | "start" | "goal" | "erase"
  const [start, setStart] = useState(null);
  const [goal, setGoal] = useState(null);
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const updateCell = useCallback(
    (row, col) => {
      setGrid((prev) => {
        const next = prev.map((r) => [...r]);
        const current = next[row][col];

        if (mode === "start") {
          // Limpiar start anterior
          if (start) next[start.row][start.col] = CELL_TYPES.EMPTY;
          if (current !== CELL_TYPES.GOAL) {
            next[row][col] = CELL_TYPES.START;
            setStart({ row, col });
          }
        } else if (mode === "goal") {
          if (goal) next[goal.row][goal.col] = CELL_TYPES.EMPTY;
          if (current !== CELL_TYPES.START) {
            next[row][col] = CELL_TYPES.GOAL;
            setGoal({ row, col });
          }
        } else if (mode === "wall") {
          if (current === CELL_TYPES.EMPTY) next[row][col] = CELL_TYPES.WALL;
        } else if (mode === "erase") {
          if (current === CELL_TYPES.WALL) next[row][col] = CELL_TYPES.EMPTY;
          if (current === CELL_TYPES.START) setStart(null);
          if (current === CELL_TYPES.GOAL) setGoal(null);
          if (current !== CELL_TYPES.EMPTY) next[row][col] = CELL_TYPES.EMPTY;
        }

        return next;
      });
    },
    [mode, start, goal]
  );

  const clearResults = useCallback((baseGrid) => {
    return baseGrid.map((row) =>
      row.map((cell) =>
        cell === CELL_TYPES.EXPLORED || cell === CELL_TYPES.PATH
          ? CELL_TYPES.EMPTY
          : cell
      )
    );
  }, []);

  const animateResult = useCallback(
    (exploredOrder, path, baseGrid) => {
      const cleaned = clearResults(baseGrid);

      // Animar exploración
      exploredOrder.forEach(({ row, col }, i) => {
        setTimeout(() => {
          setGrid((prev) => {
            const next = prev.map((r) => [...r]);
            if (
              next[row][col] !== CELL_TYPES.START &&
              next[row][col] !== CELL_TYPES.GOAL
            ) {
              next[row][col] = CELL_TYPES.EXPLORED;
            }
            return next;
          });
        }, i * 20);
      });

      // Animar la ruta final después de la exploración
      const delay = exploredOrder.length * 20;
      path.forEach(({ row, col }, i) => {
        setTimeout(() => {
          setGrid((prev) => {
            const next = prev.map((r) => [...r]);
            if (
              next[row][col] !== CELL_TYPES.START &&
              next[row][col] !== CELL_TYPES.GOAL
            ) {
              next[row][col] = CELL_TYPES.PATH;
            }
            return next;
          });
        }, delay + i * 40);
      });

      return cleaned;
    },
    [clearResults]
  );

  const search = useCallback(
    async (algorithm) => {
      if (!start || !goal) {
        setError("Debes colocar un punto de inicio y un destino.");
        return;
      }

      setError(null);
      setLoading(true);

      // Recolectar obstáculos del grid actual
      const obstacles = [];
      grid.forEach((row, r) =>
        row.forEach((cell, c) => {
          if (cell === CELL_TYPES.WALL) obstacles.push({ row: r, col: c });
        })
      );

      try {
        const { data } = await runSearch({
          rows: ROWS,
          cols: COLS,
          obstacles,
          start,
          goal,
          algorithm,
        });

        setResults(data);
        animateResult(data.explored_order, data.path, grid);
      } catch (err) {
        setError(err.response?.data?.detail || "Error al conectar con el servidor.");
      } finally {
        setLoading(false);
      }
    },
    [start, goal, grid, animateResult]
  );

  const reset = useCallback(() => {
    setGrid(buildEmptyGrid());
    setStart(null);
    setGoal(null);
    setResults(null);
    setError(null);
  }, []);

  return {
    grid,
    mode,
    setMode,
    start,
    goal,
    results,
    loading,
    error,
    updateCell,
    search,
    reset,
    rows: ROWS,
    cols: COLS,
  };
}