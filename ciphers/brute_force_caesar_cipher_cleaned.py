def decrypt(message: str) -> None:
    
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for key in range(len(LETTERS)):
        translated = ""
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol
        print(f"Decryption using Key #{key}: {translated}")


def main() -> None:
    message = input("Encrypted message: ")
    message = message.upper()
    decrypt(message)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
