


def abs_val(num):
    
    return -num if num < 0 else num


def test_abs_val():
    
    assert 0 == abs_val(0)
    assert 34 == abs_val(34)
    assert 100000000000 == abs_val(-100000000000)


if __name__ == "__main__":
    print(abs_val(-34))  
