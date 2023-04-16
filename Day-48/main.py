from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie=driver.find_element(By.ID,"cookie")
cookie_count=driver.find_element(By.ID,"money")
print(cookie_count.text)
actions = ActionChains(driver)
actions.click(cookie)
for i in range(5000):
    
    actions.perform()
