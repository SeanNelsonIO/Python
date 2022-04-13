import re


def indian_phone_validator(phone: str) -> bool:
    
    pat = re.compile(r"^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$")
    match = re.search(pat, phone)
    if match:
        return match.string == phone
    return False


if __name__ == "__main__":
    print(indian_phone_validator("+918827897895"))
