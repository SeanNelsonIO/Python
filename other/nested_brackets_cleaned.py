


def is_balanced(S):

    stack = []
    open_brackets = set({"(", "[", "{"})
    closed_brackets = set({")", "]", "}"})
    open_to_closed = dict({"{": "}", "[": "]", "(": ")"})

    for i in range(len(S)):

        if S[i] in open_brackets:
            stack.append(S[i])

        elif S[i] in closed_brackets:
            if len(stack) == 0 or (
                len(stack) > 0 and open_to_closed[stack.pop()] != S[i]
            ):
                return False

    return len(stack) == 0


def main():
    s = input("Enter sequence of brackets: ")
    if is_balanced(s):
        print(s, "is balanced")
    else:
        print(s, "is not balanced")


if __name__ == "__main__":
    main()
