from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

newList = [] #list to store veggie names

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.implicitly_wait(5) #wait for 5 seconds if element not found

#click on column header
driver.find_element(By.XPATH , "//span[text()='Veg/fruit name']").click()

#collect all veggie names -> veggieList
veggieList = driver.find_elements(By.XPATH , "//tr/td[1]")
for element in veggieList:
    newList.append(element.text)

originalList = newList.copy()  #copy of original list

#sort the veggieList -> newList
newList.sort()

#compare veggieList and newList
assert newList == originalList




















