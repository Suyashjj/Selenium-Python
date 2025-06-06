from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

#static dropdown

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
# dropdown.select_by_visible_text("Female")
dropdown.select_by_index(1)
# dropdown.select_by_value("option2") #if have value attribute in dropdown

time.sleep(5)


