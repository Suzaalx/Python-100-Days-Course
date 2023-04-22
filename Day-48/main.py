from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
URL = "http://orteil.dashnet.org/experiments/cookie/"

driver.get(URL)

cookie = driver.find_element(By.ID, "cookie")
money = driver.find_element(By.ID, "money")

timeout = time.time() + 5
play_time = time.time() + 60 * 5
while time.time() < play_time:
    cookie.click()

    if time.time() > timeout:
        items = driver.find_elements(By.CSS_SELECTOR, "#store > div:not(.grayed)")

        if len(items) > 0:
            items[-1].click()

        timeout = time.time() + 5

print("Your final score:", driver.find_element(By.ID, "cps").text)
driver.save_screenshot("result.png")