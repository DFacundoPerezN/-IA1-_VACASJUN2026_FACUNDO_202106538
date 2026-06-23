import { useMaze } from "./hooks/useMaze";
import MazeGrid from "./components/MazeGrid";
import Controls from "./components/Controls";
import Results from "./components/Results";
import "./App.css";

export default function App() {
  const {
    grid,
    mode,
    setMode,
    results,
    loading,
    error,
    updateCell,
    search,
    reset,
    resize,
    rows,
    cols,
  } = useMaze();

  return (
    <div className="app">
      <header className="app__header">
        <h1 className="app__title">
          <span className="app__title-robot">⬡</span> RoboMaze
        </h1>
        <p className="app__subtitle">
          Visualizador de algoritmos de búsqueda BFS &amp; DFS
        </p>
      </header>

      <main className="app__main">
        <Controls
          mode={mode}
          onModeChange={setMode}
          onSearch={search}
          onReset={reset}
          onResize={resize}
          rows={rows}
          cols={cols}
          loading={loading}
        />

        <div className="app__grid-wrapper">
          <MazeGrid grid={grid} onCellInteract={updateCell} />
          <p className="app__hint">
            Haz clic o arrastra para dibujar. Selecciona un modo en el panel izquierdo.
          </p>
        </div>

        <Results results={results} error={error} />
      </main>
    </div>
  );
}