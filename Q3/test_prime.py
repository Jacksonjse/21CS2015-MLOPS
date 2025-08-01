from prime import find_prime

def test_prime():
    assert find_prime(5) == True
def test_nonprime():
    assert find_prime(4) == False
def test_negative():
    assert find_prime(-1) == False
def test_zero():
    assert find_prime(0) == False