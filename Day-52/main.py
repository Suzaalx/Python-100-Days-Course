import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
 

ZILLOW_ENDPOINT = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.63417281103516%2C%22east%22%3A-122.23248518896484%2C%22south%22%3A37.656879965418064%2C%22north%22%3A37.89351359163887%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246", 
"Referer": "https://www.google.com"}
 
class ZillowData:
    def __init__(self):
        self.response = requests.get(url=ZILLOW_ENDPOINT, headers=headers)
        self.soup = BeautifulSoup(self.response.text, 'lxml')
       
        self.listings = self.soup.select(' .property-card-data')
      
        self.link_list=[listing.find_all("a") for listing in self.listings]
        self.url=[]
        self.adress=[]
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
            print(self.url)
            print(len(self.url))
    def get_adress(self):
        for link in self.link_list:
            self.adress.append(link[0].get_text())
        print(self.adress)
        print(len(self.adress))
    def get_price(self):
        self.price_list=self.soup.select('div .bqsBln span')
        
        for price in self.price_list:
            # print(price.get_text().split("+")[0].split("/")[0])
            # print(price.get_text())
            self.price.append(price.get_text().split("+")[0].split("/")[0])
        print(self.price)
        print(len(self.price))
            # print(price.get_text())
        # print(link_list)
        # for link in link_list:
        #     print(link[0].get_text())
        #     print(link[0].get("href"))
        
data=ZillowData()
data.get_endpoints()
data.get_adress()
data.get_price()
