from lib.reading_time_estimate import *

def test_empty_string():
    result = reading_time_estimate("")
    assert result == 0
