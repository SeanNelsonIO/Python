




class matrix:  
    def __init__(self, row: int, col: int, graph: list):
        self.ROW = row
        self.COL = col
        self.graph = graph

    def is_safe(self, i, j, visited) -> bool:
        return (
            0 <= i < self.ROW
            and 0 <= j < self.COL
            and not visited[i][j]
            and self.graph[i][j]
        )

    def diffs(self, i, j, visited):  
        rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]  
        colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]
        visited[i][j] = True  
        for k in range(8):
            if self.is_safe(i + rowNbr[k], j + colNbr[k], visited):
                self.diffs(i + rowNbr[k], j + colNbr[k], visited)

    def count_islands(self) -> int:  
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                if visited[i][j] is False and self.graph[i][j] == 1:
                    self.diffs(i, j, visited)
                    count += 1
        return count
