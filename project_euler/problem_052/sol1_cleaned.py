


def solution():
    
    i = 1

    while True:
        if (
            sorted(list(str(i)))
            == sorted(list(str(2 * i)))
            == sorted(list(str(3 * i)))
            == sorted(list(str(4 * i)))
            == sorted(list(str(5 * i)))
            == sorted(list(str(6 * i)))
        ):
            return i

        i += 1


if __name__ == "__main__":
    print(solution())
