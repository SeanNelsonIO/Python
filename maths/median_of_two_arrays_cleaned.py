from __future__ import annotations


def median_of_two_arrays(nums1: list[float], nums2: list[float]) -> float:
    
    all_numbers = sorted(nums1 + nums2)
    div, mod = divmod(len(all_numbers), 2)
    if mod == 1:
        return all_numbers[div]
    else:
        return (all_numbers[div] + all_numbers[div - 1]) / 2


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    array_1 = [float(x) for x in input("Enter the elements of first array: ").split()]
    array_2 = [float(x) for x in input("Enter the elements of second array: ").split()]
    print(f"The median of two arrays is: {median_of_two_arrays(array_1, array_2)}")
