
import itertools


def isCombinationValid(combination):
    
    return (
        int("".join(combination[0:2])) * int("".join(combination[2:5]))
        == int("".join(combination[5:9]))
    ) or (
        int("".join(combination[0])) * int("".join(combination[1:5]))
        == int("".join(combination[5:9]))
    )


def solution():
    

    return sum(
        {
            int("".join(pandigital[5:9]))
            for pandigital in itertools.permutations("123456789")
            if isCombinationValid(pandigital)
        }
    )


if __name__ == "__main__":
    print(solution())
