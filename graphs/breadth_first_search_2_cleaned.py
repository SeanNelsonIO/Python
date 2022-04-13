
from __future__ import annotations

from queue import Queue

G = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}


def breadth_first_search(graph: dict, start: str) -> set[str]:
    
    explored = {start}
    queue: Queue = Queue()
    queue.put(start)
    while not queue.empty():
        v = queue.get()
        for w in graph[v]:
            if w not in explored:
                explored.add(w)
                queue.put(w)
    return explored


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(breadth_first_search(G, "A"))
