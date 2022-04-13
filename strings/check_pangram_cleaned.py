


def check_pangram(
    input_str: str = "The quick brown fox jumps over the lazy dog",
) -> bool:
    
    frequency = set()
    input_str = input_str.replace(
        " ", ""
    )  
    for alpha in input_str:
        if "a" <= alpha.lower() <= "z":
            frequency.add(alpha.lower())

    return True if len(frequency) == 26 else False


def check_pangram_faster(
    input_str: str = "The quick brown fox jumps over the lazy dog",
) -> bool:
    
    flag = [False] * 26
    for char in input_str:
        if char.islower():
            flag[ord(char) - 97] = True
        elif char.isupper():
            flag[ord(char) - 65] = True
    return all(flag)


def benchmark() -> None:
    
    from timeit import timeit

    setup = "from __main__ import check_pangram, check_pangram_faster"
    print(timeit("check_pangram()", setup=setup))
    print(timeit("check_pangram_faster()", setup=setup))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    benchmark()
