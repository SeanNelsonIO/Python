
import os


def solution():
    
    script_dir = os.path.dirname(os.path.realpath(__file__))
    triangle = os.path.join(script_dir, "triangle.txt")

    with open(triangle) as f:
        triangle = f.readlines()

    a = map(lambda x: x.rstrip("\r\n").split(" "), triangle)
    a = list(map(lambda x: list(map(lambda y: int(y), x)), a))

    for i in range(1, len(a)):
        for j in range(len(a[i])):
            if j != len(a[i - 1]):
                number1 = a[i - 1][j]
            else:
                number1 = 0
            if j > 0:
                number2 = a[i - 1][j - 1]
            else:
                number2 = 0
            a[i][j] += max(number1, number2)
    return max(a[-1])


if __name__ == "__main__":
    print(solution())
