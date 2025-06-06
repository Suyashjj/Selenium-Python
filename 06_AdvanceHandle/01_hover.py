from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

actions = ActionChains(driver)
actions.move_to_element(driver.find_element(By.ID , "mousehover")).perform() #hover over element
actions.context_click(driver.find_element(By.LINK_TEXT , "Top")).perform() #right click
time.sleep(2)
actions.move_to_element(driver.find_element(By.LINK_TEXT , "Reload")).click().perform() 




















