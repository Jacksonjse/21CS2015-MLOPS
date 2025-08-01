
from factorial import factorial

def test_postive_number():
    assert factorial(5) == 120
def test_negative_number():
    assert factorial(-1) == "negative"
def test_zero():
    assert factorial(0) == 1
    print("It is a zero")