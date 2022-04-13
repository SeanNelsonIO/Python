
from __future__ import annotations

import math


def get_pascal_triangle_unique_coefficients(depth: int) -> set[int]:
    
    coefficients = {1}
    previous_coefficients = [1]
    for step in range(2, depth + 1):
        coefficients_begins_one = previous_coefficients + [0]
        coefficients_ends_one = [0] + previous_coefficients
        previous_coefficients = []
        for x, y in zip(coefficients_begins_one, coefficients_ends_one):
            coefficients.add(x + y)
            previous_coefficients.append(x + y)
    return coefficients


def get_primes_squared(max_number: int) -> list[int]:
    
    max_prime = math.isqrt(max_number)
    non_primes = [False] * (max_prime + 1)
    primes = []
    for num in range(2, max_prime + 1):
        if non_primes[num]:
            continue

        for num_counter in range(num**2, max_prime + 1, num):
            non_primes[num_counter] = True

        primes.append(num**2)
    return primes


def get_squared_primes_to_use(
    num_to_look: int, squared_primes: list[int], previous_index: int
) -> int:
    
    idx = max(previous_index, 0)

    while idx < len(squared_primes) and squared_primes[idx] <= num_to_look:
        idx += 1

    if idx == 0 and squared_primes[idx] > num_to_look:
        return -1

    if idx == len(squared_primes) and squared_primes[-1] > num_to_look:
        return -1

    return idx


def get_squarefree(
    unique_coefficients: set[int], squared_primes: list[int]
) -> set[int]:
    

    if len(squared_primes) == 0:
        return set()

    non_squarefrees = set()
    prime_squared_idx = 0
    for num in sorted(unique_coefficients):
        prime_squared_idx = get_squared_primes_to_use(
            num, squared_primes, prime_squared_idx
        )
        if prime_squared_idx == -1:
            continue
        if any(num % prime == 0 for prime in squared_primes[:prime_squared_idx]):
            non_squarefrees.add(num)

    return unique_coefficients.difference(non_squarefrees)


def solution(n: int = 51) -> int:
    
    unique_coefficients = get_pascal_triangle_unique_coefficients(n)
    primes = get_primes_squared(max(unique_coefficients))
    squarefrees = get_squarefree(unique_coefficients, primes)
    return sum(squarefrees)


if __name__ == "__main__":
    print(f"{solution() = }")
