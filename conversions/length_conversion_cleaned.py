

from collections import namedtuple

from_to = namedtuple("from_to", "from_ to")

TYPE_CONVERSION = {
    "millimeter": "mm",
    "centimeter": "cm",
    "meter": "m",
    "kilometer": "km",
    "inch": "in",
    "inche": "in",  
    "feet": "ft",
    "foot": "ft",
    "yard": "yd",
    "mile": "mi",
}

METRIC_CONVERSION = {
    "mm": from_to(0.001, 1000),
    "cm": from_to(0.01, 100),
    "m": from_to(1, 1),
    "km": from_to(1000, 0.001),
    "in": from_to(0.0254, 39.3701),
    "ft": from_to(0.3048, 3.28084),
    "yd": from_to(0.9144, 1.09361),
    "mi": from_to(1609.34, 0.000621371),
}


def length_conversion(value: float, from_type: str, to_type: str) -> float:
    
    new_from = from_type.lower().rstrip("s")
    new_from = TYPE_CONVERSION.get(new_from, new_from)
    new_to = to_type.lower().rstrip("s")
    new_to = TYPE_CONVERSION.get(new_to, new_to)
    if new_from not in METRIC_CONVERSION:
        raise ValueError(
            f"Invalid 'from_type' value: {from_type!r}.\n"
            f"Conversion abbreviations are: {', '.join(METRIC_CONVERSION)}"
        )
    if new_to not in METRIC_CONVERSION:
        raise ValueError(
            f"Invalid 'to_type' value: {to_type!r}.\n"
            f"Conversion abbreviations are: {', '.join(METRIC_CONVERSION)}"
        )
    return value * METRIC_CONVERSION[new_from].from_ * METRIC_CONVERSION[new_to].to


if __name__ == "__main__":
    import doctest

    doctest.testmod()
