from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(2) #wait for 5 seconds if element not found


driver.find_element(By.CSS_SELECTOR , ".search-keyword").send_keys("ber")
time.sleep(3)
results = driver.find_elements(By.XPATH , "//div[@class='products']/div")
count = len(results)
assert count > 0

for result in results:
    result.find_element(By.XPATH , "div/button").click() #chaining execute

driver.find_element(By.CSS_SELECTOR , "img[alt = 'Cart']").click()
driver.find_element(By.XPATH , "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR , ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR , ".promoBtn").click()

wait = WebDriverWait(driver, 10)  #Explicit wait - only for .promoInfo element
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR , ".promoInfo")))

print(driver.find_element(By.CSS_SELECTOR , ".promoInfo").text)















