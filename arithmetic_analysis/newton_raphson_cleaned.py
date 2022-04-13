



from __future__ import annotations

from decimal import Decimal
from math import *  

from sympy import diff


def newton_raphson(
    func: str, a: float | Decimal, precision: float = 10**-10
) -> float:
    
    x = a
    while True:
        x = Decimal(x) - (Decimal(eval(func)) / Decimal(eval(str(diff(func)))))
        
        if abs(eval(func)) < precision:
            return float(x)



if __name__ == "__main__":
    
    
    print(f"The root of sin(x) = 0 is {newton_raphson('sin(x)', 2)}")
    
    print(f"The root of x**2 - 5*x + 2 = 0 is {newton_raphson('x**2 - 5*x + 2', 0.4)}")
    
    print(f"The root of log(x) - 1 = 0 is {newton_raphson('log(x) - 1', 2)}")
    
    print(f"The root of exp(x) - 1 = 0 is {newton_raphson('exp(x) - 1', 0)}")
