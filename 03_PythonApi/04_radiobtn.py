from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

radiobuttons = driver.find_elements(By.CSS_SELECTOR , ".radioButton")
radiobuttons[2].click()  #directly - because we know position will not change
assert radiobuttons[2].is_selected()


#show and hide textbox
driver.find_element(By.ID , "hide-textbox").click()
assert driver.find_element(By.ID , "show-textbox").is_displayed()


time.sleep(3)

