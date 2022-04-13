
import math as m


def calc_derivative(f, a, h=0.001):
    
    return (f(a + h) - f(a - h)) / (2 * h)


def newton_raphson(f, x0=0, maxiter=100, step=0.0001, maxerror=1e-6, logsteps=False):

    a = x0  
    steps = [a]
    error = abs(f(a))
    f1 = lambda x: calc_derivative(f, x, h=step)  
    for _ in range(maxiter):
        if f1(a) == 0:
            raise ValueError("No converging solution found")
        a = a - f(a) / f1(a)  
        if logsteps:
            steps.append(a)
        if error < maxerror:
            break
    else:
        raise ValueError("Iteration limit reached, no converging solution found")
    if logsteps:
        
        return a, error, steps
    return a, error


if __name__ == "__main__":
    from matplotlib import pyplot as plt

    f = lambda x: m.tanh(x) ** 2 - m.exp(3 * x)  
    solution, error, steps = newton_raphson(
        f, x0=10, maxiter=1000, step=1e-6, logsteps=True
    )
    plt.plot([abs(f(x)) for x in steps])
    plt.xlabel("step")
    plt.ylabel("error")
    plt.show()
    print(f"solution = {{{solution:f}}}, error = {{{error:f}}}")
