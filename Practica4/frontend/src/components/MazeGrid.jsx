import { useRef, useState } from "react";
import { CELL_TYPES } from "../hooks/useMaze";
import "./MazeGrid.css";

const CELL_LABELS = {
  [CELL_TYPES.START]: "S",
  [CELL_TYPES.GOAL]: "G",
};

export default function MazeGrid({ grid, onCellInteract }) {
  const isDrawing = useRef(false);
  const [hoveredCell, setHoveredCell] = useState(null);

  const handleMouseDown = (row, col) => {
    isDrawing.current = true;
    onCellInteract(row, col);
  };

  const handleMouseEnter = (row, col) => {
    setHoveredCell(`${row}-${col}`);
    if (isDrawing.current) onCellInteract(row, col);
  };

  const handleMouseUp = () => {
    isDrawing.current = false;
  };

  return (
    <div
      className="maze-grid"
      onMouseUp={handleMouseUp}
      onMouseLeave={() => {
        isDrawing.current = false;
        setHoveredCell(null);
      }}
    >
      {grid.map((row, r) => (
        <div key={r} className="maze-row">
          {row.map((cellType, c) => (
            <div
              key={c}
              className={`maze-cell maze-cell--${cellType} ${
                hoveredCell === `${r}-${c}` ? "maze-cell--hovered" : ""
              }`}
              onMouseDown={() => handleMouseDown(r, c)}
              onMouseEnter={() => handleMouseEnter(r, c)}
            >
              {CELL_LABELS[cellType] && (
                <span className="maze-cell__label">{CELL_LABELS[cellType]}</span>
              )}
            </div>
          ))}
        </div>
      ))}
    </div>
  );
}