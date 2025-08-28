import pytest


def test_firstprogram():
    msg= "Hello"
    print(msg)
    assert msg == "Hi" ,"String not matches"

@pytest.mark.smoke
def test_secondprogram():
    a= 4
    b= 6
    assert a+2 == b ,"Count Matches"
    print(a+b)


