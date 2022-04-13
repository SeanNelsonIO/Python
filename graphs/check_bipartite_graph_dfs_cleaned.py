







def check_bipartite_dfs(graph):
    visited = [False] * len(graph)
    color = [-1] * len(graph)

    def dfs(v, c):
        visited[v] = True
        color[v] = c
        for u in graph[v]:
            if not visited[u]:
                dfs(u, 1 - c)

    for i in range(len(graph)):
        if not visited[i]:
            dfs(i, 0)

    for i in range(len(graph)):
        for j in graph[i]:
            if color[i] == color[j]:
                return False

    return True



graph = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 4: []}
print(check_bipartite_dfs(graph))
