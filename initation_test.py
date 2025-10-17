# save as invu_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    # Setup Chrome driver (webdriver-manager will install appropriate chromedriver)
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # start maximized
    # options.add_argument("--headless")  # uncomment if you want headless mode

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    try:
        wait = WebDriverWait(driver, 15)  # 15s explicit wait

        # 1) Open invu.ge
        driver.get("https://invu.ge")

        # 2) Click on the element //a[@class='desktop-login']
        login_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='desktop-login']")))
        login_link.click()
        time.sleep(5)
        
        # 3) Enter email into //input[@id='email']
        email_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='email']")))
        email_input.clear()
        email_input.send_keys("Lily.imerlishvili@gmail.com")

        # 4) Enter password into //input[@id='password']
        password_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']")))
        password_input.clear()
        password_input.send_keys("123@Test")

        # 5) Click submit //button[@type='submit']
        submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        submit_btn.click()

        # optional - wait a bit to let login complete / observe result
        time.sleep(5)
        
        # 6) Click on Templates link with Georgian text 'შაბლონები'
        ge_templates = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='desktop-nav']//a[contains(text(),'შაბლონები')]")))
        ge_templates.click()
        
         #7 Click on first template card
        first_template_card = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class, 'template-card')])[1]")))
        first_template_card.click()

        #  Wait a few seconds to observe
        time.sleep(5)
          # 8 Enter 'Lili & Gio' into the input with @placeholder
        name_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder]")))
        name_input.clear()
        name_input.send_keys("Lili & Gio")

        #Wait to observe
        time.sleep(5)
        #9 Enter 'Imerlishvili' into the element with @type='date'
        date_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='date']")))
        date_input.clear()
        date_input.send_keys("11/11/2025")  # Note: not a valid date, but per your instruction

        # Wait to observe result
        time.sleep(5) 
        
        # 10 Enter 'Imerlishvili' into input with @type='time'
        time_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='time']")))
        time_input.clear()
        time_input.send_keys("13:00")  # Note: not a valid time format
         # Wait to observe result
        time.sleep(5) 

        # 7) Click the gradient primary button
        gradient_btn_locator = (By.XPATH, "//button@class'Create Invitation')"
        )
        click_with_retry(driver, gradient_btn_locator)
        wait_overlay_gone(driver)

        # 8) Optional: verify result by waiting for a success toast or next page element
        # wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@role='status' and contains(., 'Success')]")))

        time.sleep(3)

    except Exception as e:
        # capture screenshot and page state to debug intermittent fails
        ts = int(time.time())
        try:
            driver.save_screenshot(f"/tmp/invu_fail_{ts}.png")
        except Exception:
            pass
        print("Error:", repr(e))
    finally:
        driver.quit()

if __name__ == "__main__":
    main()