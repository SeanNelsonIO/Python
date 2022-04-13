


def decimal_isolate(number, digitAmount):

    
    if digitAmount > 0:
        return round(number - int(number), digitAmount)
    return number - int(number)


if __name__ == "__main__":
    print(decimal_isolate(1.53, 0))
    print(decimal_isolate(35.345, 1))
    print(decimal_isolate(35.345, 2))
    print(decimal_isolate(35.345, 3))
    print(decimal_isolate(-14.789, 3))
    print(decimal_isolate(0, 2))
    print(decimal_isolate(-14.123, 1))
    print(decimal_isolate(-14.123, 2))
    print(decimal_isolate(-14.123, 3))
