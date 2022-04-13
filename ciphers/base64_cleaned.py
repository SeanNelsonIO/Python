B64_CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def base64_encode(data: bytes) -> bytes:
    
    
    if not isinstance(data, bytes):
        raise TypeError(
            f"a bytes-like object is required, not '{data.__class__.__name__}'"
        )

    binary_stream = "".join(bin(byte)[2:].zfill(8) for byte in data)

    padding_needed = len(binary_stream) % 6 != 0

    if padding_needed:
        
        padding = b"=" * ((6 - len(binary_stream) % 6) // 2)

        
        
        binary_stream += "0" * (6 - len(binary_stream) % 6)
    else:
        padding = b""

    
    return (
        "".join(
            B64_CHARSET[int(binary_stream[index : index + 6], 2)]
            for index in range(0, len(binary_stream), 6)
        ).encode()
        + padding
    )


def base64_decode(encoded_data: str) -> bytes:
    
    
    if not isinstance(encoded_data, bytes) and not isinstance(encoded_data, str):
        raise TypeError(
            "argument should be a bytes-like object or ASCII string, not "
            f"'{encoded_data.__class__.__name__}'"
        )

    
    
    if isinstance(encoded_data, bytes):
        try:
            encoded_data = encoded_data.decode("utf-8")
        except UnicodeDecodeError:
            raise ValueError("base64 encoded data should only contain ASCII characters")

    padding = encoded_data.count("=")

    
    if padding:
        assert all(
            char in B64_CHARSET for char in encoded_data[:-padding]
        ), "Invalid base64 character(s) found."
    else:
        assert all(
            char in B64_CHARSET for char in encoded_data
        ), "Invalid base64 character(s) found."

    
    assert len(encoded_data) % 4 == 0 and padding < 3, "Incorrect padding"

    if padding:
        
        encoded_data = encoded_data[:-padding]

        binary_stream = "".join(
            bin(B64_CHARSET.index(char))[2:].zfill(6) for char in encoded_data
        )[: -padding * 2]
    else:
        binary_stream = "".join(
            bin(B64_CHARSET.index(char))[2:].zfill(6) for char in encoded_data
        )

    data = [
        int(binary_stream[index : index + 8], 2)
        for index in range(0, len(binary_stream), 8)
    ]

    return bytes(data)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
