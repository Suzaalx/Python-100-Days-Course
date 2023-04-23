from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import os
from dotenv import load_dotenv
load_dotenv("D:/SAT/ss/Documents/docs/EnvironmentVariable/.env")


speed_url="https://www.speedtest.net/"
twitter_url="https://twitter.com/login"
email=os.getenv("twitter_email")
username=os.getenv("twitter_name")
password=os.getenv("twitter_password")
MY_OPERATOR="Worldlink"
class InternetSpeedTwitterBot:
    def __init__(self):
        self.option=Options()
        self.option.add_argument("--start-maximized")
        self.option.add_experimental_option("detach",True)
        self.option.add_argument('--ignore-certificate-errors')
        self.option.add_argument('--ignore-ssl-errors')
        self.option.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver=webdriver.Chrome(options=self.option)
        self.down=0
        self.up=0
        
    def test_internet_speed(self):
        self.driver.get(speed_url)
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME,"start-text").click()
        time.sleep(60)
        self.down=self.driver.find_element(By.CLASS_NAME,"download-speed").text
        self.up=self.driver.find_element(By.CLASS_NAME,"upload-speed").text
        print(f"Download Speed: {self.down} Upload Speed: {self.up}")


    def tweet_at_provider(self):
        self.driver.get(twitter_url)
        time.sleep(2)
        self.email=self.driver.find_element(By.XPATH,"//input[@autocomplete='username']")
        self.email.send_keys(f"{email}")
        self.email.send_keys(Keys.ENTER)
        time.sleep(2)
        self.username=self.driver.find_element(By.NAME,"text")
        self.username.send_keys(f"{username}")
        self.username.send_keys(Keys.ENTER)
        time.sleep(2)
        self.password=self.driver.find_element(By.NAME,"password")
        self.password.send_keys(f"{password}")
        self.password.send_keys(Keys.ENTER)
        time.sleep(2)
        self.tweet=self.driver.find_element(By.XPATH,"//div[contains(@aria-label, 'Tweet text')]")
        self.tweet.send_keys(f'Hey {MY_OPERATOR} .My down speed is {self.down} and up is {self.up}')
        self.button=self.driver.find_element(By.XPATH,'//div[@data-testid="tweetButtonInline"]').click()
        time.sleep(10)
        self.driver.quit()
        
bot=InternetSpeedTwitterBot()

bot.tweet_at_provider()


                
        
        
        
    
    



    

