import pytest

@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last. Like closing browser, clearing cookies")

@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Rahul", "Shetty", "rahulshettyacademy.com"]

@pytest.fixture(params=[("chrome", "Rahul"), ("Firefox", "Betty"), ("IE", "John")])
def crossBrowser(request):
    return request.param
