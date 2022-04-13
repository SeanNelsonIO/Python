

import math


def is_prime(k: int) -> bool:
    
    if k < 2 or k % 2 == 0:
        return False
    elif k == 2:
        return True
    else:
        for x in range(3, int(math.sqrt(k) + 1), 2):
            if k % x == 0:
                return False
    return True


def solution(a_limit: int = 1000, b_limit: int = 1000) -> int:
    
    longest = [0, 0, 0]  
    for a in range((a_limit * -1) + 1, a_limit):
        for b in range(2, b_limit):
            if is_prime(b):
                count = 0
                n = 0
                while is_prime((n**2) + (a * n) + b):
                    count += 1
                    n += 1
                if count > longest[0]:
                    longest = [count, a, b]
    ans = longest[1] * longest[2]
    return ans


if __name__ == "__main__":
    print(solution(1000, 1000))
