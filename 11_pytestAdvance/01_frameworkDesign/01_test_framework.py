from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_e2e(browserInstance): 
    driver = browserInstance
    #browserInstance is the fixture function , take value from conftest.py , and here we continue execution with data from conftest.py
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    
    # driver.get("https://rahulshettyacademy.com/loginpagePractise/") 
    # driver.find_element(By.ID,"username").send_keys("rahulshettyacademy")
    # driver.find_element(By.ID,"password").send_keys("learning")
    # driver.find_element(By.ID,"signInBtn").click()

    #  //a[contains(@href,'shop')]    a[href*='shop']
    driver.find_element(By.CSS_SELECTOR," a[href*='shop']").click()
    products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")

    for product in products :
        productName = product.find_element(By.XPATH, "div/h4/a").text
        if productName == "Blackberry":
            product.find_element(By.XPATH, "div/button").click()

    driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
    driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
    driver.find_element(By.ID,"country").send_keys("ind")
    wait = WebDriverWait(driver,10)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
    driver.find_element(By.LINK_TEXT,"India").click()
    driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
    driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
    successText = driver.find_element(By.CLASS_NAME,"alert-success").text
    assert "Success! Thank you!" in successText






