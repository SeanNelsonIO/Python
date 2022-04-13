from __future__ import annotations


def find_min(nums: list[int | float]) -> int | float:
    
    if len(nums) == 0:
        raise ValueError("find_min() arg is an empty sequence")
    min_num = nums[0]
    for num in nums:
        if min_num > num:
            min_num = num
    return min_num


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
