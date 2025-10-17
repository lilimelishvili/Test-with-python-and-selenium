from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
# Initialize Chrome WebDriver
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)
# Step 1: Open the website
driver.get("https://invu.ge")
time.sleep(3)
# Step 2: Click on the "Login" link
login_button = driver.find_element(By.XPATH, "//a[@href='desktop-login']")
login_button.click()
time.sleep(3)
# Step 3: Enter email
email_input = driver.find_element(By.XPATH, "//input[@id='email']")
email_input.send_keys("Lily.imerlishvili@gmail.com")
time.sleep(1)
# Step 4: Enter password
password_input = driver.find_element(By.XPATH, "//input[@id='password']")
password_input.send_keys("123@Test")
time.sleep(1)
# Step 5: Click the "Login" button
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()
time.sleep(5)
