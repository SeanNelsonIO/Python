
from __future__ import annotations


def get_totients(max_one: int) -> list[int]:
    
    totients = [0] * max_one

    for i in range(0, max_one):
        totients[i] = i

    for i in range(2, max_one):
        if totients[i] == i:
            for j in range(i, max_one, i):
                totients[j] -= totients[j] // i

    return totients


def has_same_digits(num1: int, num2: int) -> bool:
    
    return sorted(str(num1)) == sorted(str(num2))


def solution(max: int = 10000000) -> int:
    

    min_numerator = 1  
    min_denominator = 0  
    totients = get_totients(max + 1)

    for i in range(2, max + 1):
        t = totients[i]

        if i * min_denominator < min_numerator * t and has_same_digits(i, t):
            min_numerator = i
            min_denominator = t

    return min_numerator


if __name__ == "__main__":
    print(f"{solution() = }")
