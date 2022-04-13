


def method_1(boundary, steps):
    
    
    h = (boundary[1] - boundary[0]) / steps
    a = boundary[0]
    b = boundary[1]
    x_i = make_points(a, b, h)
    y = 0.0
    y += (h / 2.0) * f(a)
    for i in x_i:
        
        y += h * f(i)
    y += (h / 2.0) * f(b)
    return y


def make_points(a, b, h):
    x = a + h
    while x < (b - h):
        yield x
        x = x + h


def f(x):  
    y = (x - 0) * (x - 0)
    return y


def main():
    a = 0.0  
    b = 1.0  
    steps = 10.0  
    boundary = [a, b]  
    y = method_1(boundary, steps)
    print(f"y = {y}")


if __name__ == "__main__":
    main()
