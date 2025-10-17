from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open the website
driver.get("https://invu.ge")

# Wait for the page to load
time.sleep(2)


# Click the element with XPath //a[@href='/register']
register_link = driver.find_element(By.XPATH, "//a[@href='/register']")
register_link.click()

# Wait for the registration page to load
time.sleep(2)

# Enter 'Lili' in the input with id 'firstName'
first_name_input = driver.find_element(By.XPATH, "//input[@id='firstName']")
first_name_input.send_keys("Lili")

# Enter 'Imerlishvili' in the input with id 'lastName'
last_name_input = driver.find_element(By.XPATH, "//input[@id='lastName']")
last_name_input.send_keys("Imerlishvili")

# Enter 'Lily.imerlishvili@gmail.com' in the input with id 'email'
email_input = driver.find_element(By.XPATH, "//input[@id='email']")
email_input.send_keys("Lily.imerlishvili@gmail.com")

# Enter '123@Test' in the input with id 'password'
password_input = driver.find_element(By.XPATH, "//input[@id='password']")
password_input.send_keys("123@Test")

# Enter '123@Test' in the input with id 'confirmPassword'
confirm_password_input = driver.find_element(By.XPATH, "//input[@id='confirmPassword']")
confirm_password_input.send_keys("123@Test")

# Click the submit button with itype='submit'
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()


# Wait for the page to load after submission
time.sleep(3)

# Check if a profile has been created by looking for a profile-related element
try:
	# Example: look for a profile icon or user name element (update XPath as needed)
	profile_element = driver.find_element(By.XPATH, "//div[contains(@class, 'profile') or contains(@class, 'user') or contains(text(), 'პროფილი')]")
	print("Profile has been created successfully.")
except Exception as e:
	print("Profile creation was not detected.")

# Optionally, keep the browser open for a few seconds
time.sleep(5)

# Close the browser
driver.quit()