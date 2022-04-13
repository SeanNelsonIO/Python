


def check_bouncy(n: int) -> bool:
    
    if not isinstance(n, int):
        raise ValueError("check_bouncy() accepts only integer arguments")
    str_n = str(n)
    sorted_str_n = "".join(sorted(str_n))
    return sorted_str_n != str_n and sorted_str_n[::-1] != str_n


def solution(percent: float = 99) -> int:
    
    if not 0 < percent < 100:
        raise ValueError("solution() only accepts values from 0 to 100")
    bouncy_num = 0
    num = 1

    while True:
        if check_bouncy(num):
            bouncy_num += 1
        if (bouncy_num / num) * 100 >= percent:
            return num
        num += 1


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(f"{solution(99)}")
