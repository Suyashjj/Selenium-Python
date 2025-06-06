from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT , "Click Here").click()
windowsOpened = driver.window_handles  #get all windows handles

driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.TAG_NAME , "h3").text)
time.sleep(2)

# driver.close() #close current window
# driver.quit() #close all windows 

#switch to parent window
driver.switch_to.window(windowsOpened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME , "h3").text
time.sleep(2)


