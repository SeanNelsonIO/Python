
from __future__ import annotations

from typing import Any


def evaluate_postfix(postfix_notation: list) -> int:
    
    if not postfix_notation:
        return 0

    operations = {"+", "-", "*", "/"}
    stack: list[Any] = []

    for token in postfix_notation:
        if token in operations:
            b, a = stack.pop(), stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                if a * b < 0 and a % b != 0:
                    stack.append(a // b + 1)
                else:
                    stack.append(a // b)
        else:
            stack.append(int(token))

    return stack.pop()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
