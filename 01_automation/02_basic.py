from selenium import webdriver
import time

driver = webdriver.Chrome()   #u can change browser
driver.get("https://chatgpt.com/?oai-dm=1")
driver.maximize_window()   #window will maximize
print(driver.title)  #title will show
print(driver.current_url) #u will get url too

time.sleep(5)