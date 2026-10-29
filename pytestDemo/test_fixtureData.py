import pytest

@pytest.mark.usefixtures("dataLoad")
class TestFixtureData:

    def test_editProfile(self, dataLoad):
        print(dataLoad[0])
        print(dataLoad)