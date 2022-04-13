

from __future__ import annotations

seive = [True] * 1000001
seive[1] = False
i = 2
while i * i <= 1000000:
    if seive[i]:
        for j in range(i * i, 1000001, i):
            seive[j] = False
    i += 1


def is_prime(n: int) -> bool:
    
    return seive[n]


def list_truncated_nums(n: int) -> list[int]:
    
    str_num = str(n)
    list_nums = [n]
    for i in range(1, len(str_num)):
        list_nums.append(int(str_num[i:]))
        list_nums.append(int(str_num[:-i]))
    return list_nums


def validate(n: int) -> bool:
    
    if len(str(n)) > 3:
        if not is_prime(int(str(n)[-3:])) or not is_prime(int(str(n)[:3])):
            return False
    return True


def compute_truncated_primes(count: int = 11) -> list[int]:
    
    list_truncated_primes: list[int] = []
    num = 13
    while len(list_truncated_primes) != count:
        if validate(num):
            list_nums = list_truncated_nums(num)
            if all(is_prime(i) for i in list_nums):
                list_truncated_primes.append(num)
        num += 2
    return list_truncated_primes


def solution() -> int:
    
    return sum(compute_truncated_primes(11))


if __name__ == "__main__":
    print(f"{sum(compute_truncated_primes(11)) = }")
