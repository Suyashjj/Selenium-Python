from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

expected_list = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']  #new
actual_list = []  #check new lisk compare with expected list

driver.implicitly_wait(2)


driver.find_element(By.CSS_SELECTOR , ".search-keyword").send_keys("ber")
time.sleep(3)
results = driver.find_elements(By.XPATH , "//div[@class='products']/div")
count = len(results)
assert count > 0

for result in results:
    actual_list.append(result.find_element(By.XPATH , "h4").text) #chaining
    result.find_element(By.XPATH , "div/button").click() 
assert actual_list == expected_list

driver.find_element(By.CSS_SELECTOR , "img[alt = 'Cart']").click()
driver.find_element(By.XPATH , "//button[text()='PROCEED TO CHECKOUT']").click()

total_amt = int(driver.find_element(By.CSS_SELECTOR , ".totAmt").text)

driver.find_element(By.CSS_SELECTOR , ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR , ".promoBtn").click()

wait = WebDriverWait(driver, 10)  
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR , ".promoInfo")))


#new - to check if the total amount is greater than the discounted amount
discounted_amount = float(driver.find_element(By.CSS_SELECTOR , ".discountAmt").text)
assert total_amt > discounted_amount














