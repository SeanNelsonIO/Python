import base64


def base85_encode(string: str) -> bytes:
    
    
    return base64.a85encode(string.encode("utf-8"))


def base85_decode(a85encoded: bytes) -> str:
    
    
    return base64.a85decode(a85encoded).decode("utf-8")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
