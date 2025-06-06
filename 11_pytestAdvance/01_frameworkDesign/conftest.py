import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = None

#default browser set to chrome , if command in terminal not provided , then defaul will be chrome
# pytest 01_test_framework.py --browser_name chrome    -> (to run specific browser)
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )


@pytest.fixture( scope="function" )
def browserInstance(request):
    global driver  #globally available for every fixture
    browser_name = request.config.getoption( "browser_name" )
    service_obj = Service()
    if browser_name == "chrome":  #firefox
        driver = webdriver.Chrome( service=service_obj )
    elif browser_name == "firefox":
        driver = webdriver.Firefox( service=service_obj )

    driver.implicitly_wait( 5 )
    # driver.get( "https://rahulshettyacademy.com/loginpagePractise/" )
    yield driver  #Before test function execution , send the driver to browserInstance(our main file)
    driver.close()  #post your test function execution






