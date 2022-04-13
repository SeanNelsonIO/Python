

"""
The maximum base can be 9 because all n-digit numbers < 10^n.
Now 9**23 has 22 digits so the maximum power can be 22.
Using these conclusions, we will calculate the result.
"""


def solution(max_base: int = 10, max_power: int = 22) -> int:
    
    bases = range(1, max_base)
    powers = range(1, max_power)
    return sum(
        1 for power in powers for base in bases if len(str(base**power)) == power
    )


if __name__ == "__main__":
    print(f"{solution(10, 22) = }")
