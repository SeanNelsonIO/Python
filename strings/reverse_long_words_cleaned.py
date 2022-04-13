def reverse_long_words(sentence: str) -> str:
    
    return " ".join(
        "".join(word[::-1]) if len(word) > 4 else word for word in sentence.split()
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(reverse_long_words("Hey wollef sroirraw"))
