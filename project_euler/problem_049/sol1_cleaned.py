

from itertools import permutations
from math import floor, sqrt


def is_prime(number: int) -> bool:
    

    if number < 2:
        return False

    for i in range(2, floor(sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


def search(target: int, prime_list: list) -> bool:
    

    left, right = 0, len(prime_list) - 1
    while left <= right:
        middle = (left + right) // 2
        if prime_list[middle] == target:
            return True
        elif prime_list[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return False


def solution():
    
    prime_list = [n for n in range(1001, 10000, 2) if is_prime(n)]
    candidates = []

    for number in prime_list:
        tmp_numbers = []

        for prime_member in permutations(list(str(number))):
            prime = int("".join(prime_member))

            if prime % 2 == 0:
                continue

            if search(prime, prime_list):
                tmp_numbers.append(prime)

        tmp_numbers.sort()
        if len(tmp_numbers) >= 3:
            candidates.append(tmp_numbers)

    passed = []
    for candidate in candidates:
        length = len(candidate)
        found = False

        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    if (
                        abs(candidate[i] - candidate[j])
                        == abs(candidate[j] - candidate[k])
                        and len({candidate[i], candidate[j], candidate[k]}) == 3
                    ):
                        passed.append(
                            sorted([candidate[i], candidate[j], candidate[k]])
                        )
                        found = True

                    if found:
                        break
                if found:
                    break
            if found:
                break

    answer = set()
    for seq in passed:
        answer.add("".join([str(i) for i in seq]))

    return max(int(x) for x in answer)


if __name__ == "__main__":
    print(solution())
