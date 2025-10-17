from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open the website
driver.get("https://invu.ge")

# Wait for the page to load
time.sleep(2)


# Click the element with XPath //a[@href='/templates']
templates_link = driver.find_element(By.XPATH, "//a[@href='/templates']")
templates_link.click()

# Wait for the Templates page to load
time.sleep(3)

# Optionally print confirmation
print("Clicked 'Templates' successfully.")

# Keep the browser open for a few seconds to verify
time.sleep(5)

# Close the browser
driver.quit()

# Click the element again with XPath //div[@class='w-full h-full flex items-center justify-center p-2 sm:p-4']
second_click = driver.find_element(By.XPATH, "//div[@class='w-full h-full flex items-center justify-center p-2 sm:p-4']")
second_click.click()

# Wait for potential action
time.sleep(3)

# Print confirmation
print(" Clicked invitation card again after entering text successfully.")


# It does not click the element

