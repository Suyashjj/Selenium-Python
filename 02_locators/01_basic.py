from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/practice-project")

# ID , NAME , CLASSNAME , CSSSELECTOR , XPATH , cssselector

driver.find_element(By.ID , "name").send_keys("Hello Suyash")
driver.find_element(By.ID , "email").send_keys("basuj2039@gmail.com")
driver.find_element(By.CSS_SELECTOR, "#agreeTerms").click()
# driver.find_element(By.ID , "form-submit").click()

# For Xpath - //tagname[@attribute='value']
# For css selector - tagname[attribute='value']

driver.find_element(By.XPATH , "//button[@type='submit']").click()  

message = driver.find_element(By.CLASS_NAME , "copyright").text #get text from element
print(message)

assert "© 2025" in message  #chech text is present or not

#if there are multiple elements with same class name, then we can use find_elements to get all the elements

theme_buttons = driver.find_elements(By.CSS_SELECTOR, ".theme-btn")
if len(theme_buttons) > 4:
    theme_buttons[4].click()  # Clicks the fifth element (index 4)
else:
    print("Not enough theme-btn elements found")








time.sleep(5)


