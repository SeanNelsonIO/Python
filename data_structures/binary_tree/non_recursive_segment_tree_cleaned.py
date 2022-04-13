
from __future__ import annotations

from typing import Any, Callable, Generic, TypeVar

T = TypeVar("T")


class SegmentTree(Generic[T]):
    def __init__(self, arr: list[T], fnc: Callable[[T, T], T]) -> None:
        
        any_type: Any | T = None

        self.N: int = len(arr)
        self.st: list[T] = [any_type for _ in range(self.N)] + arr
        self.fn = fnc
        self.build()

    def build(self) -> None:
        for p in range(self.N - 1, 0, -1):
            self.st[p] = self.fn(self.st[p * 2], self.st[p * 2 + 1])

    def update(self, p: int, v: T) -> None:
        
        p += self.N
        self.st[p] = v
        while p > 1:
            p = p // 2
            self.st[p] = self.fn(self.st[p * 2], self.st[p * 2 + 1])

    def query(self, l: int, r: int) -> T | None:  
        
        l, r = l + self.N, r + self.N  

        res: T | None = None
        while l <= r:  
            if l % 2 == 1:
                res = self.st[l] if res is None else self.fn(res, self.st[l])
            if r % 2 == 0:
                res = self.st[r] if res is None else self.fn(res, self.st[r])
            l, r = (l + 1) // 2, (r - 1) // 2
        return res


if __name__ == "__main__":
    from functools import reduce

    test_array = [1, 10, -2, 9, -3, 8, 4, -7, 5, 6, 11, -12]

    test_updates = {
        0: 7,
        1: 2,
        2: 6,
        3: -14,
        4: 5,
        5: 4,
        6: 7,
        7: -10,
        8: 9,
        9: 10,
        10: 12,
        11: 1,
    }

    min_segment_tree = SegmentTree(test_array, min)
    max_segment_tree = SegmentTree(test_array, max)
    sum_segment_tree = SegmentTree(test_array, lambda a, b: a + b)

    def test_all_segments() -> None:
        
        for i in range(len(test_array)):
            for j in range(i, len(test_array)):
                min_range = reduce(min, test_array[i : j + 1])
                max_range = reduce(max, test_array[i : j + 1])
                sum_range = reduce(lambda a, b: a + b, test_array[i : j + 1])
                assert min_range == min_segment_tree.query(i, j)
                assert max_range == max_segment_tree.query(i, j)
                assert sum_range == sum_segment_tree.query(i, j)

    test_all_segments()

    for index, value in test_updates.items():
        test_array[index] = value
        min_segment_tree.update(index, value)
        max_segment_tree.update(index, value)
        sum_segment_tree.update(index, value)
        test_all_segments()
