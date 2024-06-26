""" test file for calculate age """
from app.calculate_age import get_age

def test_get_age():
    """ this test assert age is calculated corectly """
    # Given.
    yyyy, mm, dd = map(int, "1996/07/11".split("/"))
    # When.
    age = get_age(yyyy, mm, dd)
    # Then.
    assert age == 28
	