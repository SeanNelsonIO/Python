from collections import deque


def tarjan(g):
    

    n = len(g)
    stack = deque()
    on_stack = [False for _ in range(n)]
    index_of = [-1 for _ in range(n)]
    lowlink_of = index_of[:]

    def strong_connect(v, index, components):
        index_of[v] = index  
        lowlink_of[v] = index  
        index += 1
        stack.append(v)
        on_stack[v] = True

        for w in g[v]:
            if index_of[w] == -1:
                index = strong_connect(w, index, components)
                lowlink_of[v] = (
                    lowlink_of[w] if lowlink_of[w] < lowlink_of[v] else lowlink_of[v]
                )
            elif on_stack[w]:
                lowlink_of[v] = (
                    lowlink_of[w] if lowlink_of[w] < lowlink_of[v] else lowlink_of[v]
                )

        if lowlink_of[v] == index_of[v]:
            component = []
            w = stack.pop()
            on_stack[w] = False
            component.append(w)
            while w != v:
                w = stack.pop()
                on_stack[w] = False
                component.append(w)
            components.append(component)
        return index

    components = []
    for v in range(n):
        if index_of[v] == -1:
            strong_connect(v, 0, components)

    return components


def create_graph(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
    return g


if __name__ == "__main__":
    
    n_vertices = 7
    source = [0, 0, 1, 2, 3, 3, 4, 4, 6]
    target = [1, 3, 2, 0, 1, 4, 5, 6, 5]
    edges = [(u, v) for u, v in zip(source, target)]
    g = create_graph(n_vertices, edges)

    assert [[5], [6], [4], [3, 2, 1, 0]] == tarjan(g)
