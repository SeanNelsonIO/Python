


def perfect(number: int) -> bool:
    
    return sum(i for i in range(1, number // 2 + 1) if number % i == 0) == number


if __name__ == "__main__":
    print("Program to check whether a number is a Perfect number or not...")
    number = int(input("Enter number: ").strip())
    print(f"{number} is {'' if perfect(number) else 'not '}a Perfect Number.")
