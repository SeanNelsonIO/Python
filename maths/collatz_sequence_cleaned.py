from __future__ import annotations


def collatz_sequence(n: int) -> list[int]:
    

    if not isinstance(n, int) or n < 1:
        raise Exception("Sequence only defined for natural numbers")

    sequence = [n]
    while n != 1:
        n = 3 * n + 1 if n & 1 else n // 2
        sequence.append(n)
    return sequence


def main():
    n = 43
    sequence = collatz_sequence(n)
    print(sequence)
    print(f"collatz sequence from {n} took {len(sequence)} steps.")


if __name__ == "__main__":
    main()
