

import operator as op


def Solve(Postfix):
    Stack = []
    Div = lambda x, y: int(x / y)  
    Opr = {
        "^": op.pow,
        "*": op.mul,
        "/": Div,
        "+": op.add,
        "-": op.sub,
    }  

    
    print("Symbol".center(8), "Action".center(12), "Stack", sep=" | ")
    print("-" * (30 + len(Postfix)))

    for x in Postfix:
        if x.isdigit():  
            Stack.append(x)  
            
            print(x.rjust(8), ("push(" + x + ")").ljust(12), ",".join(Stack), sep=" | ")
        else:
            B = Stack.pop()  
            
            print("".rjust(8), ("pop(" + B + ")").ljust(12), ",".join(Stack), sep=" | ")

            A = Stack.pop()  
            
            print("".rjust(8), ("pop(" + A + ")").ljust(12), ",".join(Stack), sep=" | ")

            Stack.append(
                str(Opr[x](int(A), int(B)))
            )  
            
            print(
                x.rjust(8),
                ("push(" + A + x + B + ")").ljust(12),
                ",".join(Stack),
                sep=" | ",
            )

    return int(Stack[0])


if __name__ == "__main__":
    Postfix = input("\n\nEnter a Postfix Equation (space separated) = ").split(" ")
    print("\n\tResult = ", Solve(Postfix))
