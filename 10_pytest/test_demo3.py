#Fixture -> are used as setup and teardown for test cases

import pytest

@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo1(self):
        print("I will execute steps in fixtureDemo method")

    def test_fixtureDemo2(self):
        print("I will execute steps in fixtureDemo method")

    def test_fixtureDemo3(self):
        print("I will execute steps in fixtureDemo method")

    def test_fixtureDemo4(self):
        print("I will execute steps in fixtureDemo method")