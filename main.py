from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = Options()
# chrome_options.add_argument('--disable-search-engine-choice-screen')
chrome_options.add_argument('--no-sandbox')
service = Service('chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(options=chrome_options,service=service)


driver.get('https://demoqa.com/login')

# 1. Ensure the window is maximized to avoid element overlapping
driver.maximize_window()

# 2. Wait for and fill Username
username_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,'userName')))
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", username_field)
username_field.clear()
username_field.send_keys('sampleandsample')

# 3. Use JavaScript to scroll and fill Password (bypasses most overlay issues)
password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", password_field)
password_field.clear()
password_field.send_keys('Sample@123')

# 4. Handle the Login Button using a JavaScript click
# This is the most reliable way to click if elements are obscured by footer ads
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,'login')))
driver.execute_script("arguments[0].click();", login_button)


input("Press Enter to close the browser")
driver.quit()

