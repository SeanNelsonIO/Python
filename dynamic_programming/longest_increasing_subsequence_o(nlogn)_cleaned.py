





from __future__ import annotations


def CeilIndex(v, l, r, key):  
    while r - l > 1:
        m = (l + r) // 2
        if v[m] >= key:
            r = m
        else:
            l = m  
    return r


def LongestIncreasingSubsequenceLength(v: list[int]) -> int:
    
    if len(v) == 0:
        return 0

    tail = [0] * len(v)
    length = 1

    tail[0] = v[0]

    for i in range(1, len(v)):
        if v[i] < tail[0]:
            tail[0] = v[i]
        elif v[i] > tail[length - 1]:
            tail[length] = v[i]
            length += 1
        else:
            tail[CeilIndex(tail, -1, length - 1, v[i])] = v[i]

    return length


if __name__ == "__main__":
    import doctest

    doctest.testmod()
