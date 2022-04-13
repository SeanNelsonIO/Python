import base64


def base32_encode(string: str) -> bytes:
    

    
    
    return base64.b32encode(string.encode("utf-8"))


def base32_decode(encoded_bytes: bytes) -> str:
    

    
    
    return base64.b32decode(encoded_bytes).decode("utf-8")


if __name__ == "__main__":
    test = "Hello World!"
    encoded = base32_encode(test)
    print(encoded)

    decoded = base32_decode(encoded)
    print(decoded)
