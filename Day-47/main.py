import requests
from bs4 import BeautifulSoup
import os
import smtplib
from dotenv import load_dotenv
load_dotenv("D:/SAT/ss/Documents/docs/EnvironmentVariable/.env")
password=os.getenv("email_password")
my_email="regasir12@gmail.com"
def email(price):
    
    print("working")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=f"{password}")
        connection.sendmail(from_addr=my_email,
                        to_addrs="sujalxetry00@gmail.com",
                        msg=f"Subject:Price Drop Alert\n\nThe price of Nintendo Switch Pro Controller has dropped to {price}")
        
        


headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9"
}

response=requests.get("https://camelcamelcamel.com/Nintendo-Switch-Pro-Controller/product/B01NAWKYZ0",headers=headers)
soup = BeautifulSoup(response.text,"html.parser")
print(soup.prettify())
cost=soup.find(name="span",class_="green")
price=cost.get_text().split("$")[1]
print(price)
if price<="60":
    email(price)