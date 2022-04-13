
from __future__ import annotations

from collections import namedtuple


def electric_power(voltage: float, current: float, power: float) -> tuple:
    
    result = namedtuple("result", "name value")
    if (voltage, current, power).count(0) != 1:
        raise ValueError("Only one argument must be 0")
    elif power < 0:
        raise ValueError(
            "Power cannot be negative in any electrical/electronics system"
        )
    elif voltage == 0:
        return result("voltage", power / current)
    elif current == 0:
        return result("current", power / voltage)
    elif power == 0:
        return result("power", float(round(abs(voltage * current), 2)))
    else:
        raise ValueError("Exactly one argument must be 0")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
