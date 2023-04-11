import os
from dotenv import load_dotenv
import requests
import smtplib
from email.mime.text import MIMEText
load_dotenv("D:/SAT/ss/Documents/docs/EnvironmentVariable/.env")
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_api = os.getenv("Stock_api")
news=""


#finds the closing value of stock of yesterday and day before yesterday
stock_data=requests.get(url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&outputsize=compact&apikey={stock_api}")
stock=stock_data.json()

yesterday = list(stock["Time Series (Daily)"].values())[0]
day_before = list(stock["Time Series (Daily)"].values())[1]
# print(day_before)
yesterday_stock=list(yesterday.values())[3]
day_before=list(day_before.values())[3]
# print(yesterday_stock)

    


#finds percentage by which stock increased or decreased yesterday from the day before yesterday

if yesterday_stock> day_before:
    perc= (float(yesterday_stock)- float(day_before))/float(day_before)* 100
    percentage= f"Increased by : {round(perc,1)}"
    
else:
    perc= (float(day_before)-float(yesterday_stock))/float(yesterday_stock)* 100
    percentage= f"Decreased by: {round(perc,1)}"
    
#adds the first three news article and their link to message of Tesla..
news_api= os.getenv("News_api")

news_data=requests.get(url=f"https://newsapi.org/v2/everything?q=tesla&from=2023-03-11&sortBy=publishedAt&language=en&apiKey={news_api}")
for n in range (3):
    title=news_data.json()['articles'][n]['title']
    title_url=news_data.json()['articles'][n]['url']
    desc=news_data.json()['articles'][n]["description"]
    news+= f'{n+1}. {title}\nDescription: {desc}\nUrl: {title_url}\n\n'

# Send a seperate message with the percentage change and each article's title and description to your phone number. 
print(percentage)
print(news)

news = news.encode('ascii', 'ignore').decode('ascii')


#sends email with percentage change and latest news 
my_email="regasir12@gmail.com"
password=os.getenv("email_password")

def email():
    
    print("HH")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=f"{password}")
        connection.sendmail(from_addr=my_email,
                        to_addrs="sujalxetry00@gmail.com",
                        msg=f"Subject:Stock Alert\n\nTesla {percentage}\n\n{news}\n.")
        
        
email()







