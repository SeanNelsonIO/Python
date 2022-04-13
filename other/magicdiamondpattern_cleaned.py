



def floyd(n):
    
    for i in range(0, n):
        for j in range(0, n - i - 1):  
            print(" ", end="")
        for k in range(0, i + 1):  
            print("* ", end="")
        print()



def reverse_floyd(n):
    
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):  
            print("* ", end="")
        print()
        for k in range(n - i + 1, 0, -1):  
            print(" ", end="")



def pretty_print(n):
    
    if n <= 0:
        print("       ...       ....        nothing printing :(")
        return
    floyd(n)  
    reverse_floyd(n)  


if __name__ == "__main__":
    print(r"| /\ | |- |  |-  |--| |\  /| |-")
    print(r"|/  \| |- |_ |_  |__| | \/ | |_")
    K = 1
    while K:
        user_number = int(input("enter the number and , and see the magic : "))
        print()
        pretty_print(user_number)
        K = int(input("press 0 to exit... and 1 to continue..."))

    print("Good Bye...")
