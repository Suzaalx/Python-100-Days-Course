from selenium import webdriver

from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
speed_url="https://www.speedtest.net/"
twitter_url="https://twitter.com/login"

# driver.get(speed_url)
# go=driver.find_element(By.CLASS_NAME,"start-text")
# go.click()
# #wait for 120 seconds
# time.sleep(10)
# download_speed=driver.find_element(By.CLASS_NAME,"download-speed")
# download_speed_text=download_speed.text
# upload_speed=driver.find_element(By.CLASS_NAME,"upload-speed")
# upload_speed_text=upload_speed.text
# print(f"Download Speed: {download_speed_text} Upload Speed: {upload_speed_text}")

def twitter():
    driver.get(twitter_url)
    time.sleep(5)
    driver.find_element(By.XPATH,"//input[@autocomplete='username']").send_keys('user')
twitter()
