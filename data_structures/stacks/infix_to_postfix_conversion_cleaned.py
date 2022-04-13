

from .balanced_parentheses import balanced_parentheses
from .stack import Stack


def precedence(char: str) -> int:
    
    return {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}.get(char, -1)


def infix_to_postfix(expression_str: str) -> str:
    
    if not balanced_parentheses(expression_str):
        raise ValueError("Mismatched parentheses")
    stack: Stack[str] = Stack()
    postfix = []
    for char in expression_str:
        if char.isalpha() or char.isdigit():
            postfix.append(char)
        elif char == "(":
            stack.push(char)
        elif char == ")":
            while not stack.is_empty() and stack.peek() != "(":
                postfix.append(stack.pop())
            stack.pop()
        else:
            while not stack.is_empty() and precedence(char) <= precedence(stack.peek()):
                postfix.append(stack.pop())
            stack.push(char)
    while not stack.is_empty():
        postfix.append(stack.pop())
    return " ".join(postfix)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    expression = "a+b*(c^d-e)^(f+g*h)-i"

    print("Infix to Postfix Notation demonstration:\n")
    print("Infix notation: " + expression)
    print("Postfix notation: " + infix_to_postfix(expression))
