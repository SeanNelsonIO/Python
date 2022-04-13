

import math


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y}, {self.z})"


def distance(a: Point, b: Point) -> float:
    return math.sqrt(abs((b.x - a.x) ** 2 + (b.y - a.y) ** 2 + (b.z - a.z) ** 2))


def test_distance() -> None:
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
