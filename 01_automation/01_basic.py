from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service

# #way2
# service_obj = Service("C:\\Users\\suyas\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
# driver = webdriver.Chrome(service = service_obj)

#way 1
driver = webdriver.Chrome() 
driver.get("https://smart-summarizer-silk.vercel.app/")
time.sleep(5)