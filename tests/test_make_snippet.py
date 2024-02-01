from lib.make_snippet import *

def test_empty_string_returns_empty():
    result = make_snippet("")
    assert result == ""

def test_five_word_string():
    result = make_snippet("One, two, three, four, five")
    assert result == "One, two, three, four, five"

def test_six_or_more():
    result = make_snippet("one, two, three, four, five, six, seven")
    assert result == "one, two, three, four, five, ..."
