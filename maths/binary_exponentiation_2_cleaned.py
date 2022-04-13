


def b_expo(a, b):
    res = 0
    while b > 0:
        if b & 1:
            res += a

        a += a
        b >>= 1

    return res


def b_expo_mod(a, b, c):
    res = 0
    while b > 0:
        if b & 1:
            res = ((res % c) + (a % c)) % c

        a += a
        b >>= 1

    return res

