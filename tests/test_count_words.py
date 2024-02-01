from lib.count_words import *

def test_zero_words():
    result = count_words(" ")
    assert result == 0

def test_some_words():
    result = count_words("one, two, three, four")
    assert result == 4