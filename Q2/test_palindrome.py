import unittest
from palindrome import palindrome


def test_StringOdd():
    assert palindrome("kayak") == True 
def testStringEven():
    assert palindrome("hannah") == True
def testDigits():
    assert palindrome("1234") == False
def testSpecialCharacters():
    assert palindrome("$2$2$") == True