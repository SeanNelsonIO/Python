from __future__ import annotations



def find_max(nums: list[int | float], left: int, right: int) -> int | float:
    
    if len(nums) == 0:
        raise ValueError("find_max() arg is an empty sequence")
    if (
        left >= len(nums)
        or left < -len(nums)
        or right >= len(nums)
        or right < -len(nums)
    ):
        raise IndexError("list index out of range")
    if left == right:
        return nums[left]
    mid = (left + right) >> 1  
    left_max = find_max(nums, left, mid)  
    right_max = find_max(nums, mid + 1, right)  

    return left_max if left_max >= right_max else right_max


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
