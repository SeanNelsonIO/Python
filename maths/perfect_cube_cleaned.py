def perfect_cube(n: int) -> bool:
    
    val = n ** (1 / 3)
    return (val * val * val) == n


if __name__ == "__main__":
    print(perfect_cube(27))
    print(perfect_cube(4))
