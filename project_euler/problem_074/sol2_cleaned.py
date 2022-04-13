

factorial_cache: dict[int, int] = {}
factorial_sum_cache: dict[int, int] = {}


def factorial(a: int) -> int:
    

    
    if a < 0:
        raise ValueError("Invalid negative input!", a)

    if a in factorial_cache:
        return factorial_cache[a]

    
    if a == 0:
        factorial_cache[a] = 1
    else:
        
        temporary_number = a
        temporary_computation = 1

        while temporary_number > 0:
            temporary_computation *= temporary_number
            temporary_number -= 1

        factorial_cache[a] = temporary_computation
    return factorial_cache[a]


def factorial_sum(a: int) -> int:
    
    if a in factorial_sum_cache:
        return factorial_sum_cache[a]
    
    fact_sum = 0

    """ Convert a in string to iterate on its digits
        convert the digit back into an int
        and add its factorial to fact_sum.
    """
    for i in str(a):
        fact_sum += factorial(int(i))
    factorial_sum_cache[a] = fact_sum
    return fact_sum


def solution(chain_length: int = 60, number_limit: int = 1000000) -> int:
    

    
    chain_counter = 0

    for i in range(1, number_limit + 1):

        
        chain_set = {i}
        len_chain_set = 1
        last_chain_element = i

        
        new_chain_element = factorial_sum(last_chain_element)

        
        

        while new_chain_element not in chain_set and len_chain_set <= chain_length:
            chain_set.add(new_chain_element)

            len_chain_set += 1
            last_chain_element = new_chain_element
            new_chain_element = factorial_sum(last_chain_element)

        
        
        if len_chain_set == chain_length:
            chain_counter += 1

    return chain_counter


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{solution()}")
