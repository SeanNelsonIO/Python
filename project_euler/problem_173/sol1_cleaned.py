


from math import ceil, sqrt


def solution(limit: int = 1000000) -> int:
    
    answer = 0

    for outer_width in range(3, (limit // 4) + 2):
        if outer_width**2 > limit:
            hole_width_lower_bound = max(ceil(sqrt(outer_width**2 - limit)), 1)
        else:
            hole_width_lower_bound = 1
        if (outer_width - hole_width_lower_bound) % 2:
            hole_width_lower_bound += 1

        answer += (outer_width - hole_width_lower_bound - 2) // 2 + 1

    return answer


if __name__ == "__main__":
    print(f"{solution() = }")
