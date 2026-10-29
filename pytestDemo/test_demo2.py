import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_thirdProgram():
    msg = "Hello"
    assert msg == 'Hi', "Test failed because msg is not equal to Hi"

def test_fourthCreditCard():
    a = 4
    b = 6
    assert a + 3 == 6, "Addition of 2 variabled do not match expected result"

@pytest.fixture()
def setup():
    print("I will be executed first")

def test_fixtureDemo(setup):
    print("I will execute after setup. I will execute steps from fixtureDemo method")