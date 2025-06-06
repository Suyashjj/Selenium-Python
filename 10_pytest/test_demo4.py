#data driven fixture
import pytest

@pytest.mark.usefixtures("dataLoad")
class TestExample:
   def test_editProfile(self, dataLoad): #u have to decalare dataload , if returning data
        print(dataLoad[0])
        # print(dataLoad)


