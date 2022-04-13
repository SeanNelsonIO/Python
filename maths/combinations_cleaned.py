
from math import factorial


def combinations(n: int, k: int) -> int:
    

    
    
    if n < k or k < 0:
        raise ValueError("Please enter positive integers for n and k where n >= k")
    return int(factorial(n) / ((factorial(k)) * (factorial(n - k))))


if __name__ == "__main__":

    print(
        "\nThe number of five-card hands possible from a standard",
        f"fifty-two card deck is: {combinations(52, 5)}",
    )

    print(
        "\nIf a class of 40 students must be arranged into groups of",
        f"4 for group projects, there are {combinations(40, 4)} ways",
        "to arrange them.\n",
    )

    print(
        "If 10 teams are competing in a Formula One race, there",
        f"are {combinations(10, 3)} ways that first, second and",
        "third place can be awarded.\n",
    )
