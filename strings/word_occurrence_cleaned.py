

from collections import defaultdict


def word_occurence(sentence: str) -> dict:
    
    occurrence: dict = defaultdict(int)
    
    for word in sentence.split():
        occurrence[word] += 1
    return occurrence


if __name__ == "__main__":
    for word, count in word_occurence("INPUT STRING").items():
        print(f"{word}: {count}")
