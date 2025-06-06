from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from login import LoginPage
import json
import os
import pytest

# Load the test data from the json file
test_data_path = os.path.join(os.path.dirname(__file__), 'test_main.json')
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data['data']

@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item): 
    driver = browserInstance
    # driver.get("https://rahulshettyacademy.com/loginpagePractise/")  #declared in conftest.py
    loginPage = LoginPage(driver) 
    loginPage.getTitle()
    shopPage = loginPage.login(test_list_item['userEmail'], test_list_item['userPassword'])

    # Handle potential password change pop-up error
    try:
        ok_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='OK']"))
        )
        ok_button.click()
    except Exception as e:
        print(f"Password change pop-up not found: {str(e)}")
    
    shopPage.add_product_to_cart(test_list_item['productName'])
    shopPage.getTitle()
    checkout_confirmation = shopPage.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validate_order()