
from __future__ import annotations


def quick_sort(collection: list) -> list:
    
    if len(collection) < 2:
        return collection
    pivot = collection.pop()  
    greater: list[int] = []  
    lesser: list[int] = []  
    for element in collection:
        (greater if element > pivot else lesser).append(element)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(quick_sort(unsorted))
