from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Configure Chrome options (optional)
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # open browser maximized
# chrome_options.add_argument("--headless")  # uncomment to run without opening browser window

# Initialize Chrome WebDriver
service = Service()  # it will automatically use chromedriver from PATH if installed
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the website
driver.get("https://invu.ge")

# Wait for a few seconds so you can see it
time.sleep(5)

# Close the browser
driver.quit()
# Click the Register button
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(4)

# Click on the "Register" link
register_button = driver.find_element(By.XPATH, "//a[@href='/register']")
register_button.click()

# Wait for the registration page to load
time.sleep(5)

# Close the browser
driver.quit()
# Enter "Lika" into the first name field
first_name_input = driver.find_element(By.XPATH, "//input[@id='firstName']")
first_name_input.send_keys("Lika")
time.sleep(2)

# Optional: keep the browser open for a few seconds to verify visually
time.sleep(5)

# Close the browser
driver.quit()

# Enter "Epitashvili" into the last name field
last_name_input = driver.find_element(By.XPATH, "//input[@id='lastName']")
last_name_input.send_keys("Epitashvili")
time.sleep(2)

# Optional: Wait to visually confirm
time.sleep(5)

# Close the browser
driver.quit()
# Enter "Lily.imerlishvili@gmail.com" into the email field
email_input = driver.find_element(By.XPATH, "//input[@id='email']")
email_input.send_keys("Lily.imerlishvili@gmail.com")
time.sleep(2)

# Optional: Wait to visually confirm
time.sleep(5)

# Close the browser
driver.quit()

# Enter "123@Test" into the password field
password_input = driver.find_element(By.XPATH, "//input[@id='password']")
password_input.send_keys("123@Test")
time.sleep(2)

# Optional: Wait to visually confirm
time.sleep(5)

# Close the browser
driver.quit()

# Enter "123@Test" into the confirm password field
confirm_password_input = driver.find_element(By.XPATH, "//input[@id='confirmPassword']")
confirm_password_input.send_keys("123@Test")
time.sleep(2)

# Optional: Wait to visually confirm fields are filled
time.sleep(5)

# Close the browser
driver.quit()

# Click the "Register" button
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()
time.sleep(5)

# Optional: Verify registration result (e.g., redirected to homepage)
print(" Registration form submitted successfully")

# Close the browser
driver.quit()
# Verify registration success
current_url = driver.current_url
page_source = driver.page_source

if ("welcome" in page_source.lower() 
    or "success" in page_source.lower() 
    or "home" in current_url.lower()):
    print(" Registration successful! User redirected or success message found.")
else:
    print(" Registration failed or no confirmation detected.")

# Close the browser
driver.quit()