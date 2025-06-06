from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

#headless mode - to run in background
options = webdriver.ChromeOptions()  
options.add_argument("headless")
options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=options)  #give options to chrome

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)") #covert in js - to scroll
driver.get_screenshot_as_file("selenium1.png")  #take screenshot
time.sleep(2)



















