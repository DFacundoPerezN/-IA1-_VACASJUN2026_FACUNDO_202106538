#Modelo de Resultado de Búsqueda (SearchResult)

from dataclasses import dataclass, field
from cell import Cell


@dataclass
class SearchResult:
    algorithm: str
    found: bool
    path: list[Cell] = field(default_factory=list)
    explored_order: list[Cell] = field(default_factory=list)  # orden en que se visitaron los nodos
    nodes_explored: int = 0
    execution_time_ms: float = 0.0

    def to_dict(self) -> dict:
        return {
            "algorithm": self.algorithm,
            "found": self.found,
            "path": [c.to_dict() for c in self.path],
            "path_length": len(self.path),
            "explored_order": [c.to_dict() for c in self.explored_order],
            "nodes_explored": self.nodes_explored,
            "execution_time_ms": round(self.execution_time_ms, 4),
        }