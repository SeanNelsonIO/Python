


def euclidean_gcd(a: int, b: int) -> int:
    
    while b:
        a, b = b, a % b
    return a


def euclidean_gcd_recursive(a: int, b: int) -> int:
    
    return a if b == 0 else euclidean_gcd_recursive(b, a % b)


def main():
    print(f"euclidean_gcd(3, 5) = {euclidean_gcd(3, 5)}")
    print(f"euclidean_gcd(5, 3) = {euclidean_gcd(5, 3)}")
    print(f"euclidean_gcd(1, 3) = {euclidean_gcd(1, 3)}")
    print(f"euclidean_gcd(3, 6) = {euclidean_gcd(3, 6)}")
    print(f"euclidean_gcd(6, 3) = {euclidean_gcd(6, 3)}")

    print(f"euclidean_gcd_recursive(3, 5) = {euclidean_gcd_recursive(3, 5)}")
    print(f"euclidean_gcd_recursive(5, 3) = {euclidean_gcd_recursive(5, 3)}")
    print(f"euclidean_gcd_recursive(1, 3) = {euclidean_gcd_recursive(1, 3)}")
    print(f"euclidean_gcd_recursive(3, 6) = {euclidean_gcd_recursive(3, 6)}")
    print(f"euclidean_gcd_recursive(6, 3) = {euclidean_gcd_recursive(6, 3)}")


if __name__ == "__main__":
    main()
