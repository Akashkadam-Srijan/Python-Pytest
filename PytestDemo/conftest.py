import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will executing first")
    yield # execute at the last
    print("I will execute the last")


@pytest.fixture(scope= "class")
def dataload():
    print("User profile is being created")
    return ["Akash", "Kadam", "test@gmail.com"]

@pytest.fixture(params=["Chrome", "Firefox"])
def crossbrowser(request):
    return request.param
