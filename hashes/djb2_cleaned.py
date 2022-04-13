


def djb2(s: str) -> int:
    
    hash = 5381
    for x in s:
        hash = ((hash << 5) + hash) + ord(x)
    return hash & 0xFFFFFFFF
