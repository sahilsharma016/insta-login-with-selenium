from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

login_url = "https://www.instagram.com/"
driver = webdriver.Chrome()
driver.get(login_url)

username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))

# enter your username here 
username_field.send_keys("forexample@gmail.com")

password_field = driver.find_element(By.NAME, "password")

# enter your password here
password_field.send_keys("forexample")

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()


WebDriverWait(driver, 10).until(EC.url_contains("instagram.com"))

driver.execute_script("window.open('about:blank', '_blank');")
new_window_handle = driver.window_handles[-1]
WebDriverWait(driver ,4)
driver.switch_to.window(new_window_handle)

driver.get("https://www.instagram.com/")


WebDriverWait(driver, 10).until(EC.url_contains("instagram.com"))
time.sleep(10)
driver.refresh()

# Handle 'Not Now' notification
try:
    time.sleep(5)
    not_now_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']")))
    not_now_button.click()
    print("Clicked on 'Not Now' button")
except Exception as e:
    print("No 'Not Now' button found on the page or it's not clickable.", e)

#will uncomment later 
input("Press Enter to close the browser...")
driver.quit()
