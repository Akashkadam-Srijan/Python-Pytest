import pytest


# 1. Any pytest file should start with test_
# 2. Pytest method names should start with test
# 3. Any code should be wrapped in method only

@pytest.mark.smoke
def test_firstprogram(setup):
    print("Hello")

@pytest.mark.skip
@pytest.mark.xfail
def test_secondprogram():
    print("Good Morning")



