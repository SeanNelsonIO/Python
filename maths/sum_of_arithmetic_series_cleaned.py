
def sum_of_series(first_term, common_diff, num_of_terms):
    
    sum = (num_of_terms / 2) * (2 * first_term + (num_of_terms - 1) * common_diff)
    
    return sum


def main():
    print(sum_of_series(1, 1, 10))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
