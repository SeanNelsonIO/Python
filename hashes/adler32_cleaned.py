


def adler32(plain_text: str) -> int:
    
    MOD_ADLER = 65521
    a = 1
    b = 0
    for plain_chr in plain_text:
        a = (a + ord(plain_chr)) % MOD_ADLER
        b = (b + a) % MOD_ADLER
    return (b << 16) | a
