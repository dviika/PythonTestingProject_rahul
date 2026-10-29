#any pytest file should start with test_ or end with _test
#pytest method names should start with test
#any code should be wrapped in method only
#method names should be descriptive and not too long
# -k stands for method names execution py.test -k CreditCard -v -s
# -s stands for print statement execution
# -v stands for verbose more metadata
# you can run specific test file py.test  <filename> py.test test_demo1.py -v -s
#you can mark(tag) your test cases with @pytest.mark.<tagname> and run specific test cases with py.test -m <tagname> -v -s
#you can skip the test cases with @pytest.mark.skip
#you can skip the test cases with @pytest.mark.skipif(condition, reason="reason for skipping")
#you can run the test cases with expected failure with @pytest.mark.xfail
#fixtures are used to execute some code before and after the test cases. It is used for setup and teardown activities. Fixtures can be defined in conftest.py file and can be used across multiple test files.
#data driven testing can be done using @pytest.mark.parametrize decorator. It is used to run the same test case with different sets of data. The data can be passed as a list of tuples or a list of dictionaries. The test case will be executed for each set of data.
#when you define fixture in conftest.py file, you don't need to import it in your test files. It will be automatically available for all the test files in the same directory and sub-directories.


import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Helloo")

@pytest.mark.xfail
def test_CreditCardQuestionnaire():
    print("Do you have sour cream?")

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
