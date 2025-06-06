from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.implicitly_wait(6)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr") #switch to frame
driver.find_element(By.CSS_SELECTOR , "#tinymce").clear()
driver.find_element(By.ID , "tinymce").send_keys("able to change text")
time.sleep(2)

driver.switch_to.default_content() #switch to default content
print(driver.find_element(By.TAG_NAME , "h3").text)
time.sleep(2)

