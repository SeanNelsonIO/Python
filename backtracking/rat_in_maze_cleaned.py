from __future__ import annotations


def solve_maze(maze: list[list[int]]) -> bool:
    
    size = len(maze)
    
    solutions = [[0 for _ in range(size)] for _ in range(size)]
    solved = run_maze(maze, 0, 0, solutions)
    if solved:
        print("\n".join(str(row) for row in solutions))
    else:
        print("No solution exists!")
    return solved


def run_maze(maze: list[list[int]], i: int, j: int, solutions: list[list[int]]) -> bool:
    
    size = len(maze)
    
    if i == j == (size - 1):
        solutions[i][j] = 1
        return True

    lower_flag = (not (i < 0)) and (not (j < 0))  
    upper_flag = (i < size) and (j < size)  

    if lower_flag and upper_flag:
        
        block_flag = (not (solutions[i][j])) and (not (maze[i][j]))
        if block_flag:
            
            solutions[i][j] = 1

            
            if (
                run_maze(maze, i + 1, j, solutions)
                or run_maze(maze, i, j + 1, solutions)
                or run_maze(maze, i - 1, j, solutions)
                or run_maze(maze, i, j - 1, solutions)
            ):
                return True

            solutions[i][j] = 0
            return False
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
