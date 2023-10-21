import pytest
from dayoffs.utils.date_utils import is_valid_date


def test_is_valid_date():
    # test valid dates
    assert is_valid_date("2022-12-31", "%Y-%m-%d") == True
    assert is_valid_date("31/12/2022", "%d/%m/%Y") == True
    assert is_valid_date("12/31/2022", "%m/%d/%Y") == True

    # test invalid dates
    assert is_valid_date("2022/12/31", "%Y-%m-%d") == False
    assert is_valid_date("31-12-2022", "%d/%m/%Y") == False
    assert is_valid_date("12-31-2022", "%m/%d/%Y") == False

    # test invalid format
    assert is_valid_date("2022/12/31", "") == False
