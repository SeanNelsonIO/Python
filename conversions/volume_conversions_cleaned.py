

from collections import namedtuple

from_to = namedtuple("from_to", "from_ to")

METRIC_CONVERSION = {
    "cubicmeter": from_to(1, 1),
    "litre": from_to(0.001, 1000),
    "kilolitre": from_to(1, 1),
    "gallon": from_to(0.00454, 264.172),
    "cubicyard": from_to(0.76455, 1.30795),
    "cubicfoot": from_to(0.028, 35.3147),
    "cup": from_to(0.000236588, 4226.75),
}


def volume_conversion(value: float, from_type: str, to_type: str) -> float:
    
    if from_type not in METRIC_CONVERSION:
        raise ValueError(
            f"Invalid 'from_type' value: {from_type!r}  Supported values are:\n"
            + ", ".join(METRIC_CONVERSION)
        )
    if to_type not in METRIC_CONVERSION:
        raise ValueError(
            f"Invalid 'to_type' value: {to_type!r}.  Supported values are:\n"
            + ", ".join(METRIC_CONVERSION)
        )
    return value * METRIC_CONVERSION[from_type].from_ * METRIC_CONVERSION[to_type].to


if __name__ == "__main__":
    import doctest

    doctest.testmod()
