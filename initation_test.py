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

# Click the first template card using XPath (//div[contains(@class, "template-card")])[1]
first_template_card = driver.find_element(By.XPATH, '(//div[contains(@class, "template-card")])[1]')
first_template_card.click()

# Wait for the invitation editor or next page to load
time.sleep(3)

# Print confirmation
print("✅ Clicked on the first template card successfully.")

# Keep the browser open briefly
time.sleep(5)

# Close the browser
driver.quit()

#TEST TS