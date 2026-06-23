import "./Results.css";

export default function Results({ results, error }) {
  if (error) {
    return (
      <div className="results results--error">
        <span className="results__error-icon">⚠</span>
        <p>{error}</p>
      </div>
    );
  }

  if (!results) {
    return (
      <div className="results results--empty">
        <p>Configura el laberinto y ejecuta un algoritmo para ver los resultados.</p>
      </div>
    );
  }

  const stats = [
    {
      label: "Algoritmo",
      value: results.algorithm,
    },
    {
      label: "Ruta encontrada",
      value: results.found ? "✓ Sí" : "✗ No",
      highlight: results.found ? "success" : "fail",
    },
    {
      label: "Longitud de ruta",
      value: results.found ? `${results.path_length} celdas` : "—",
    },
    {
      label: "Nodos explorados",
      value: results.nodes_explored,
    },
    {
      label: "Tiempo de ejecución",
      value: `${results.execution_time_ms} ms`,
    },
  ];

  return (
    <div className="results">
      <h3 className="results__title">Resultado</h3>
      <div className="results__stats">
        {stats.map((s) => (
          <div key={s.label} className="stat">
            <span className="stat__label">{s.label}</span>
            <span className={`stat__value ${s.highlight ? `stat__value--${s.highlight}` : ""}`}>
              {s.value}
            </span>
          </div>
        ))}
      </div>

      {results.found && results.path_length > 0 && (
        <div className="results__path">
          <h4 className="results__path-title">Ruta completa</h4>
          <div className="results__path-cells">
            {results.path.map((cell, i) => (
              <span key={i} className="path-cell">
                ({cell.row},{cell.col})
                {i < results.path.length - 1 && <span className="path-arrow">→</span>}
              </span>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}