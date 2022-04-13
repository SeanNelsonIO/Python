



from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def strong_password_detector(password: str, min_length: int = 8) -> str:
    

    if len(str(password)) < 8:
        return "Your Password must be at least 8 characters long"

    upper = any(char in ascii_uppercase for char in password)
    lower = any(char in ascii_lowercase for char in password)
    num = any(char in digits for char in password)
    spec_char = any(char in punctuation for char in password)

    if upper and lower and num and spec_char:
        return "This is a strong Password"

    else:
        return (
            "Password should contain UPPERCASE, lowercase, "
            "numbers, special characters"
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
