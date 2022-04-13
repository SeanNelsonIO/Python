from __future__ import annotations


def abs_max(x: list[int]) -> int:
    
    if len(x) == 0:
        raise ValueError("abs_max() arg is an empty sequence")
    j = x[0]
    for i in x:
        if abs(i) > abs(j):
            j = i
    return j


def abs_max_sort(x: list[int]) -> int:
    
    if len(x) == 0:
        raise ValueError("abs_max_sort() arg is an empty sequence")
    return sorted(x, key=abs)[-1]


def main():
    a = [1, 2, -11]
    assert abs_max(a) == -11
    assert abs_max_sort(a) == -11


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    main()
