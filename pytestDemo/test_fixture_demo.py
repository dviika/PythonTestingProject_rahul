import pytest

@pytest.mark.usefixtures("setup")
class TestExample:


    def test_fixtureDemo(self, setup):
        print("I will execute after setup. I will execute steps from fixtureDemo method")

    def test_fixtureDemo2(self, setup):
        print("I will execute after setup. I will execute steps from fixtureDemo method")

    def test_fixtureDemo3(self, setup):
        print("I will execute after setup. I will execute steps from fixtureDemo method")