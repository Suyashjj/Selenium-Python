#Java Popup/ Browser Alert

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

name = "Suyash"
driver.find_element(By.CSS_SELECTOR , "#name").send_keys(name)
driver.find_element(By.ID , "alertbtn").click()
alert = driver.switch_to.alert
alerttext = alert.text
print(alerttext)
assert name in alerttext
alert.accept()


time.sleep(3)


