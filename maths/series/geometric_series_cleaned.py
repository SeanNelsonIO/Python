


from __future__ import annotations


def geometric_series(
    nth_term: float | int,
    start_term_a: float | int,
    common_ratio_r: float | int,
) -> list[float | int]:
    
    if not all((nth_term, start_term_a, common_ratio_r)):
        return []
    series: list[float | int] = []
    power = 1
    multiple = common_ratio_r
    for _ in range(int(nth_term)):
        if series == []:
            series.append(start_term_a)
        else:
            power += 1
            series.append(float(start_term_a * multiple))
            multiple = pow(float(common_ratio_r), power)
    return series


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    nth_term = float(input("Enter the last number (n term) of the Geometric Series"))
    start_term_a = float(input("Enter the starting term (a) of the Geometric Series"))
    common_ratio_r = float(
        input("Enter the common ratio between two terms (r) of the Geometric Series")
    )
    print("Formula of Geometric Series => a + ar + ar^2 ... +ar^n")
    print(geometric_series(nth_term, start_term_a, common_ratio_r))
