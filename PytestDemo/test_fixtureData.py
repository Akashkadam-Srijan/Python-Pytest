import pytest


@pytest.mark.usefixtures("dataload")
class TestData:

    def test_editProfile(self,dataload):
        print(dataload)