import pytest

@pytest.mark.usefixtures("setup")
class TestFixture:

    def test_fixturedemo1(self):
        print("I will be execute steps in fixture Demo1 method")

    def test_fixturedemo2(self):
        print("I will be execute steps in fixture Demo2 method")

    def test_fixturedemo3(self):
        print("I will be execute steps in fixture Demo3 method")

    def test_fixturedemo4(self):
        print("I will be execute steps in fixture Demo4 method")
