







from queue import Queue


def checkBipartite(graph):
    queue = Queue()
    visited = [False] * len(graph)
    color = [-1] * len(graph)

    def bfs():
        while not queue.empty():
            u = queue.get()
            visited[u] = True

            for neighbour in graph[u]:

                if neighbour == u:
                    return False

                if color[neighbour] == -1:
                    color[neighbour] = 1 - color[u]
                    queue.put(neighbour)

                elif color[neighbour] == color[u]:
                    return False

        return True

    for i in range(len(graph)):
        if not visited[i]:
            queue.put(i)
            color[i] = 0
            if bfs() is False:
                return False

    return True


if __name__ == "__main__":
    
    print(checkBipartite({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}))
