

from collections.abc import Iterable


def check_matrix(matrix):
    
    if matrix and isinstance(matrix, Iterable):
        if isinstance(matrix[0], Iterable):
            prev_len = 0
            for row in matrix:
                if prev_len == 0:
                    prev_len = len(row)
                    result = True
                else:
                    result = prev_len == len(row)
        else:
            result = True
    else:
        result = False

    return result


def spiralPrint(a):
    if check_matrix(a) and len(a) > 0:
        matRow = len(a)
        if isinstance(a[0], Iterable):
            matCol = len(a[0])
        else:
            for dat in a:
                print(dat),
            return

        
        for i in range(0, matCol):
            print(a[0][i]),
        
        for i in range(1, matRow):
            print(a[i][matCol - 1]),
        
        if matRow > 1:
            for i in range(matCol - 2, -1, -1):
                print(a[matRow - 1][i]),
        
        for i in range(matRow - 2, 0, -1):
            print(a[i][0]),
        remainMat = [row[1 : matCol - 1] for row in a[1 : matRow - 1]]
        if len(remainMat) > 0:
            spiralPrint(remainMat)
        else:
            return
    else:
        print("Not a valid matrix")
        return



if __name__ == "__main__":
    a = ([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12])
    spiralPrint(a)
