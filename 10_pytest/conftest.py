import pytest

@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")  #pre-requisite before yield
    yield
    print("I will be executing last")  #post-requisite after yield

@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["John", "Doe", "john@doe.com"]

# @pytest.fixture(params=["chrome", "firefox", "IE"])
@pytest.fixture(params=[("chrome", "John"), ("firefox", "Doe"), ("IE", "Jane")])
def crossBrowser(request):
    return request.param
