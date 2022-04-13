

import os


def solution():
    
    with open(os.path.dirname(__file__) + "/grid.txt") as f:
        l = []  
        for i in range(20):
            l.append([int(x) for x in f.readline().split()])

        maximum = 0

        
        for i in range(20):
            for j in range(17):
                temp = l[i][j] * l[i][j + 1] * l[i][j + 2] * l[i][j + 3]
                if temp > maximum:
                    maximum = temp

        
        for i in range(17):
            for j in range(20):
                temp = l[i][j] * l[i + 1][j] * l[i + 2][j] * l[i + 3][j]
                if temp > maximum:
                    maximum = temp

        
        for i in range(17):
            for j in range(17):
                temp = l[i][j] * l[i + 1][j + 1] * l[i + 2][j + 2] * l[i + 3][j + 3]
                if temp > maximum:
                    maximum = temp

        
        for i in range(17):
            for j in range(3, 20):
                temp = l[i][j] * l[i + 1][j - 1] * l[i + 2][j - 2] * l[i + 3][j - 3]
                if temp > maximum:
                    maximum = temp
        return maximum


if __name__ == "__main__":
    print(solution())
