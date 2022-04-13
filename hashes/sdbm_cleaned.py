


def sdbm(plain_text: str) -> int:
    
    hash = 0
    for plain_chr in plain_text:
        hash = ord(plain_chr) + (hash << 6) + (hash << 16) - hash
    return hash
