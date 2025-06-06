from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")


driver.find_element(By.LINK_TEXT , "Forgot password?").click()
driver.find_element(By.XPATH , "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR , "form div:nth-child(2) input").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR , "#confirmPassword").send_keys("Hello@1234")
driver.find_element(By.XPATH , "//button[@type='submit']").click()
# select by Link_text in xpath -> //button[text() = 'Save New Password'] 



time.sleep(5)


