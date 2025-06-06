#Doing Sum Validation

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(2) 


driver.find_element(By.CSS_SELECTOR , ".search-keyword").send_keys("ber")
time.sleep(3)
results = driver.find_elements(By.XPATH , "//div[@class='products']/div")
count = len(results)
assert count > 0

for result in results:
    result.find_element(By.XPATH , "div/button").click() #chaining execute

driver.find_element(By.CSS_SELECTOR , "img[alt = 'Cart']").click()
driver.find_element(By.XPATH , "//button[text()='PROCEED TO CHECKOUT']").click()

#Sum Validation  - //new
prices = driver.find_elements(By.CSS_SELECTOR , "tr td:nth-child(5) p")
sum = 0
for price in prices:
    price.text
    sum += int(price.text)  #str to int
print(sum)
total_amt = int(driver.find_element(By.CSS_SELECTOR , ".totAmt").text)
assert sum == total_amt


driver.find_element(By.CSS_SELECTOR , ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR , ".promoBtn").click()

wait = WebDriverWait(driver, 10)  
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR , ".promoInfo")))
















