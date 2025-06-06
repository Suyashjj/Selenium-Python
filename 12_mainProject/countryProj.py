from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://countryproject-coral.vercel.app/")
driver.maximize_window()
driver.implicitly_wait(4)

# Step 1: Click on 'Country' link
time.sleep(1)
country_link = driver.find_element(By.XPATH, "//a[@href='/country']")
country_link.click()

# Step 2: Search for 'indi'
search_bar = driver.find_element(By.XPATH, "//input[@placeholder='Search countries...']")
search_bar.click()
search_bar.send_keys("indi")

time.sleep(2)

# Step 3: Click 'Desc' button
desc_button = driver.find_element(By.XPATH, "//button[normalize-space()='Desc']")
desc_button.click()

# time.sleep(2)

# Step 4: Click on India's 'Read More' button
time.sleep(2)
read_more_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Read More')]")
read_more_buttons[0].click()  # Click first Read More button (India after Desc sort)

# Step 5: Extract and print India's detailed information
time.sleep(1)

print("\n" + "="*50)
print("INDIA - DETAILED INFORMATION")
print("="*50)

# Get all text from the page and extract information
body_text = driver.find_element(By.TAG_NAME, "body").text
lines = [line.strip() for line in body_text.split('\n') if line.strip()]

# Extract specific information from the text lines
for line in lines:
    if "Native Names:" in line:
        print(f"Native Names: {line.replace('Native Names:', '').strip()}")
    elif "Population:" in line:
        print(f"Population: {line.replace('Population:', '').strip()}")
    elif "Region:" in line and "Sub Region:" not in line:
        print(f"Region: {line.replace('Region:', '').strip()}")
    elif "Sub Region:" in line:
        print(f"Sub Region: {line.replace('Sub Region:', '').strip()}")
    elif "Capital:" in line:
        print(f"Capital: {line.replace('Capital:', '').strip()}")
    elif "Top Level Domain:" in line:
        print(f"Top Level Domain: {line.replace('Top Level Domain:', '').strip()}")
    elif "Currencies:" in line:
        print(f"Currencies: {line.replace('Currencies:', '').strip()}")
    elif "Languages:" in line:
        print(f"Languages: {line.replace('Languages:', '').strip()}")

print("="*50)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "footer"))  # or any stable element
)

driver.quit()