

from collections import namedtuple

from_to = namedtuple("from_to", "from_ to")

PRESSURE_CONVERSION = {
    "atm": from_to(1, 1),
    "pascal": from_to(0.0000098, 101325),
    "bar": from_to(0.986923, 1.01325),
    "kilopascal": from_to(0.00986923, 101.325),
    "megapascal": from_to(9.86923, 0.101325),
    "psi": from_to(0.068046, 14.6959),
    "inHg": from_to(0.0334211, 29.9213),
    "torr": from_to(0.00131579, 760),
}


def pressure_conversion(value: float, from_type: str, to_type: str) -> float:
    
    if from_type not in PRESSURE_CONVERSION:
        raise ValueError(
            f"Invalid 'from_type' value: {from_type!r}  Supported values are:\n"
            + ", ".join(PRESSURE_CONVERSION)
        )
    if to_type not in PRESSURE_CONVERSION:
        raise ValueError(
            f"Invalid 'to_type' value: {to_type!r}.  Supported values are:\n"
            + ", ".join(PRESSURE_CONVERSION)
        )
    return (
        value * PRESSURE_CONVERSION[from_type].from_ * PRESSURE_CONVERSION[to_type].to
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
