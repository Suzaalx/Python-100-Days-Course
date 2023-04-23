import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import os
from dotenv import load_dotenv
load_dotenv("D:/SAT/ss/Documents/docs/EnvironmentVariable/.env")
# doc form url
DOC_URL="https://docs.google.com/forms/d/e/1FAIpQLSeZTbQ-KaH3wWnfSJhgC0QzdyIYuem-1xa4UD2Gbl2Ke56Hrw/viewform?usp=sf_link"
#zillow website endpoint with header so that we can scrape the data
ZILLOW_ENDPOINT = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.63417281103516%2C%22east%22%3A-122.23248518896484%2C%22south%22%3A37.656879965418064%2C%22north%22%3A37.89351359163887%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246", 
"Referer": "https://www.google.com"}
 
 
class ZillowData:
    def __init__(self):
        self.response = requests.get(url=ZILLOW_ENDPOINT, headers=headers)
        self.soup = BeautifulSoup(self.response.text, 'lxml')
       # scraping the links and 
        self.listings = self.soup.select(' .property-card-data')
        self.link_list=[listing.find_all("a") for listing in self.listings]
        self.price_list=self.soup.select('div .bqsBln span')
        self.url=[]
        self.address=[]
        self.price=[]
        
    def get_endpoints(self):
        for link in self.link_list:
                #using link[0] because link is a list with one element, so while it may be confusing if you print both link[0] and link ,you will understand link[0] is necessary to access the elements inside the list
                # print(link[0])
                # print(link)
            if link[0].get("href").startswith("https"):
                self.url.append(link[0].get("href"))
                    
            else:
                self.url.append("https://www.zillow.com"+link[0].get("href"))
        return(self.url)
        
    def get_address(self):
        for link in self.link_list:
            self.address.append(link[0].get_text())
        return self.address
    
    def get_price(self):
        for price in self.price_list:
            self.price.append(price.get_text().split("+")[0].split("/")[0])
        return self.price
    

class fill_data :
    #it may seem quite confusing but well ignore all the arguments and experimental stuffs. It just keep throwing errors in my console which is pretty annoying so we just add them to ignore them
    def __init__(self):
        self.option=Options()
        self.option.add_argument("--start-maximized")
        #this keeps the chrome window open even after the program is done
        self.option.add_experimental_option("detach",True)
        self.option.add_argument('--ignore-certificate-errors')
        self.option.add_argument('--ignore-ssl-errors')
        self.option.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver=webdriver.Chrome(options=self.option)
        #getting the data which we will use to fill the form
        self.data=ZillowData()
        self.address=self.data.get_address()
        self.price=self.data.get_price()
        self.url=self.data.get_endpoints()
       

    def fill_form(self):
        self.driver.get(DOC_URL)
        #zip can iterate through multiple lists at the same time. 
        for address,price,link in zip(self.address,self.price,self.url):
            time.sleep(1)
            #just copy pasting the xpath of the input fields in the google form.
            #Using xpath is quite easy but it does not work for all the websites.it would have been quite convenient if we coould tho.
            
            address_keys = self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
            address_keys.send_keys(address)
            price_keys=self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_keys.send_keys(price)
            link_keys=self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_keys.send_keys(link)
            submit=self.driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            submit.click()
            time.sleep(1)
            another_response=self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            another_response.click()
            
    def close(self):
        self.driver.close()

fill=fill_data()
fill.fill_form()
fill.close()