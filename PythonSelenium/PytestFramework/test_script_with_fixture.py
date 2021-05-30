import pytest

#scope="Function" : this setup function will execute before each test function
#@pytest.fixture(scope="function")
#scope="module": in this scope setup function will be executed before initiate the test cases execution.
@pytest.fixture(scope="module")
def setup():
    print("\n Pre-requisite done")
    yield   # teardown , it always call at the end.
    print("\n We are closing the automation")


def test_case1(setup):
    a = 40
    b = 50
    print("addition :", a+b)
    print("_"*50)


def test_case2(setup):
    a = 40
    b = 50
    print("multiplication:", a*b)
    print("_"*50)


def test_case3(setup):
    a = 40
    b = 50
    print("division:", a//b)
    print("_"*50)