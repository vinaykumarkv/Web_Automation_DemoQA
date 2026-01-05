from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import keyboard

class WebAutomation:
    def __init__(self):
        self.download_path = os.getcwd()
        self.prefs = {'download.default_directory': self.download_path}

        self.chrome_options = Options()
        # chrome_options.add_argument('--disable-search-engine-choice-screen')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_experimental_option('prefs', self.prefs)

        self.service = Service('chromedriver-win64/chromedriver.exe')
        self.driver = webdriver.Chrome(options=self.chrome_options, service=self.service)

    def login(self, username, password):
        self.username = username
        self.password = password
        self.driver.get('https://demoqa.com/login')

        self.driver.maximize_window()

        self.username_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'userName')))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", self.username_field)
        self.username_field.clear()
        self.username_field.send_keys(self.username)

        self.password_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", self.password_field)
        self.password_field.clear()
        self.password_field.send_keys(self.password)

        # login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,'login')))
        self.login_button = self.driver.find_element(By.ID, 'login')
        self.driver.execute_script("arguments[0].click();", self.login_button)

    def fillform(self, fullname, email, currentaddress, permanentaddress):
        # locate elements dropdown and textbox
        self.fullname = fullname
        self.email = email
        self.currentaddress = currentaddress
        self.permanentaddress = permanentaddress
        self.element_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div/div[1]')))
        self.driver.execute_script("arguments[0].click();", self.element_field)
        text_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div[1]/div/ul/li[1]/span')))
        self.driver.execute_script("arguments[0].click();", text_field)

        # locate the form fields
        self.name_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'userName')))

        self.user_email_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'userEmail')))

        self.user_current_address_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'currentAddress')))

        self.user_permanent_address_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'permanentAddress')))

        self.submit_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'submit')))

        # fill in the form fields
        self.name_field.send_keys(self.fullname)
        self.user_email_field.send_keys(self.email)
        self.user_current_address_field.send_keys(self.currentaddress)
        self.user_permanent_address_field.send_keys(self.permanentaddress)
        # submit_field.click()
        self.driver.execute_script("arguments[0].click();", self.submit_field)

    def download(self):
        # upload / download

        def clean_demoqa_ui(driver):
            # This script removes the footer, the fixed ad banner, and any Google ad containers
            script = """
            var selectors = ['#fixedban', 'footer', '#adplus-anchor', '.google-auto-placed'];
            selectors.forEach(function(selector) {
                var elements = document.querySelectorAll(selector);
                elements.forEach(function(el) { el.remove(); });
            });
            """
            driver.execute_script(script)

        clean_demoqa_ui(self.driver)

        self.upload_download_option = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'item-7'))
        )

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", self.upload_download_option)

        self.driver.execute_script("arguments[0].click();", self.upload_download_option)

        self.download_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'downloadButton')))
        # upload_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID,'uploadFile')))

        self.download_button.click()

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    driver = WebAutomation()
    driver.login("sampleandsample", "Sample@123")
    driver.fillform("sampleandsample", "sampleandsample@sample.com", "123, 1st cross, sample street, pincode123", "123, 1st cross, sample street, pincode123")
    driver.download()
    while True:
        if keyboard.is_pressed('q'):
            print("Exiting...")
            break
    driver.close()


