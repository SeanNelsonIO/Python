






edges = {"a": ["c", "b"], "b": ["d", "e"], "c": [], "d": [], "e": []}
vertices = ["a", "b", "c", "d", "e"]


def topological_sort(start, visited, sort):
    
    current = start
    
    visited.append(current)
    neighbors = edges[current]
    for neighbor in neighbors:
        
        if neighbor not in visited:
            sort = topological_sort(neighbor, visited, sort)
    
    sort.append(current)
    
    if len(visited) != len(vertices):
        for vertice in vertices:
            if vertice not in visited:
                sort = topological_sort(vertice, visited, sort)
    
    return sort


if __name__ == "__main__":
    sort = topological_sort("a", [], [])
    print(sort)
