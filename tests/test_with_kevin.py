import pytest
from lib.with_kevin import *



def test_access_over_16():
    result = check_date_for_access("1999-01-01")
    message = "Access granted"
    assert result == message

def test_deny_under_16():
    result = check_date_for_access("2022-02-01")
    message = "Access denied, you are 2, you must be at least 16"
    assert result == message

def test_for_value_error():
    with pytest.raises(ValueError, match="time data 'error' does not match format '%Y-%m-%d'"):
        check_date_for_access("error")