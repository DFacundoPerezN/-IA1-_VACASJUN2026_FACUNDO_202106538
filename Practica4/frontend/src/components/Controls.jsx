import "./Controls.css";

const MODES = [
  { id: "start",  label: "Inicio",   color: "#22c55e", icon: "S" },
  { id: "goal",   label: "Destino",  color: "#f59e0b", icon: "G" },
  { id: "wall",   label: "Muro",     color: "#475569", icon: "▪" },
  { id: "erase",  label: "Borrar",   color: "#ef4444", icon: "✕" },
];

export default function Controls({ mode, onModeChange, onSearch, onReset, onResize, rows, cols, loading }) {
  const handleResize = (e, type) => {
    const val = Math.min(30, Math.max(4, Number(e.target.value)));
    if (type === "rows") onResize(val, cols);
    else onResize(rows, val);
  };

  return (
    <div className="controls">
      <section className="controls__section">
        <h3 className="controls__label">Tamaño del laberinto</h3>
        <div className="controls__size">
          <label className="size-field">
            <span>Filas</span>
            <input type="number" min={4} max={30} value={rows} onChange={(e) => handleResize(e, "rows")} />
          </label>
          <label className="size-field">
            <span>Columnas</span>
            <input type="number" min={4} max={30} value={cols} onChange={(e) => handleResize(e, "cols")} />
          </label>
        </div>
      </section>

      <section className="controls__section">
        <h3 className="controls__label">Modo de edición</h3>
        <div className="controls__modes">
          {MODES.map((m) => (
            <button
              key={m.id}
              className={`mode-btn ${mode === m.id ? "mode-btn--active" : ""}`}
              style={{ "--mode-color": m.color }}
              onClick={() => onModeChange(m.id)}
            >
              <span className="mode-btn__icon">{m.icon}</span>
              <span className="mode-btn__label">{m.label}</span>
            </button>
          ))}
        </div>
      </section>

      <section className="controls__section">
        <h3 className="controls__label">Ejecutar algoritmo</h3>
        <div className="controls__actions">
          <button
            className="run-btn run-btn--bfs"
            onClick={() => onSearch("bfs")}
            disabled={loading}
          >
            {loading ? "Ejecutando..." : "▶ BFS"}
          </button>
          <button
            className="run-btn run-btn--dfs"
            onClick={() => onSearch("dfs")}
            disabled={loading}
          >
            {loading ? "Ejecutando..." : "▶ DFS"}
          </button>
          <button
            className="run-btn run-btn--astar"
            onClick={() => onSearch("astar")}
            disabled={loading}
          >
            {loading ? "Ejecutando..." : "▶ A*"}
          </button>
        </div>
      </section>

      <button className="reset-btn" onClick={onReset} disabled={loading}>
        ↺ Reiniciar laberinto
      </button>

      <div className="controls__legend">
        <h3 className="controls__label">Leyenda</h3>
        <div className="legend-items">
          <div className="legend-item"><span className="legend-dot" style={{ background: "#22c55e" }} />Inicio</div>
          <div className="legend-item"><span className="legend-dot" style={{ background: "#f59e0b" }} />Destino</div>
          <div className="legend-item"><span className="legend-dot" style={{ background: "#475569" }} />Muro</div>
          <div className="legend-item"><span className="legend-dot" style={{ background: "#1e3a5f" }} />Explorado</div>
          <div className="legend-item"><span className="legend-dot" style={{ background: "#3b82f6" }} />Ruta</div>
        </div>
      </div>
    </div>
  );
}