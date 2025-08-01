from fibo import fibonnaci

def test_postitive():
    assert fibonnaci(4) == [0, 1, 1, 2]
def test_negative():
    assert fibonnaci(-1) == False
def test_zero():
    assert fibonnaci(0) == 0