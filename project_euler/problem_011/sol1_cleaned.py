

import os


def largest_product(grid):
    nColumns = len(grid[0])
    nRows = len(grid)

    largest = 0
    lrDiagProduct = 0
    rlDiagProduct = 0

    
    
    for i in range(nColumns):
        for j in range(nRows - 3):
            vertProduct = grid[j][i] * grid[j + 1][i] * grid[j + 2][i] * grid[j + 3][i]
            horzProduct = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]

            
            if i < nColumns - 3:
                lrDiagProduct = (
                    grid[i][j]
                    * grid[i + 1][j + 1]
                    * grid[i + 2][j + 2]
                    * grid[i + 3][j + 3]
                )

            
            if i > 2:
                rlDiagProduct = (
                    grid[i][j]
                    * grid[i - 1][j + 1]
                    * grid[i - 2][j + 2]
                    * grid[i - 3][j + 3]
                )

            maxProduct = max(vertProduct, horzProduct, lrDiagProduct, rlDiagProduct)
            if maxProduct > largest:
                largest = maxProduct

    return largest


def solution():
    
    grid = []
    with open(os.path.dirname(__file__) + "/grid.txt") as file:
        for line in file:
            grid.append(line.strip("\n").split(" "))

    grid = [[int(i) for i in grid[j]] for j in range(len(grid))]

    return largest_product(grid)


if __name__ == "__main__":
    print(solution())
