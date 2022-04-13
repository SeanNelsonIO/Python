import base64


def base16_encode(inp: str) -> bytes:
    
    
    return base64.b16encode(inp.encode("utf-8"))


def base16_decode(b16encoded: bytes) -> str:
    
    
    return base64.b16decode(b16encoded).decode("utf-8")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
