from __future__ import annotations


def find_max(nums: list[int | float]) -> int | float:
    
    if len(nums) == 0:
        raise ValueError("find_max() arg is an empty sequence")
    max_num = nums[0]
    for x in nums:
        if x > max_num:
            max_num = x
    return max_num


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
