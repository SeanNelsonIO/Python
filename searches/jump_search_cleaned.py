

import math


def jump_search(arr: list, x: int) -> int:
    

    n = len(arr)
    step = int(math.floor(math.sqrt(n)))
    prev = 0
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.floor(math.sqrt(n)))
        if prev >= n:
            return -1

    while arr[prev] < x:
        prev = prev + 1
        if prev == min(step, n):
            return -1
    if arr[prev] == x:
        return prev
    return -1


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    arr = [int(item) for item in user_input.split(",")]
    x = int(input("Enter the number to be searched:\n"))
    res = jump_search(arr, x)
    if res == -1:
        print("Number not found!")
    else:
        print(f"Number {x} is at index {res}")
