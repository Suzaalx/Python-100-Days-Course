import os
from dotenv import load_dotenv
import requests
import smtplib
load_dotenv("D:/SAT/ss/Documents/docs/EnvironmentVariable/.env")
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_api = os.getenv("Stock_api")
message=""
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_data=requests.get(url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&outputsize=compact&apikey={stock_api}")
stock=stock_data.json()



yesterday = list(stock["Time Series (Daily)"].values())[0]
day_before = list(stock["Time Series (Daily)"].values())[1]
# print(day_before)
yesterday_stock=list(yesterday.values())[3]
day_before=list(day_before.values())[3]
# print(yesterday_stock)

    




if yesterday_stock> day_before:
    percentage= f"Increased by: {(float(yesterday_stock)/ float(day_before))* 100}"
    
else:
    percentage= f"Decreased by: {(float(day_before)/ float(yesterday_stock))* 100}"
    
    

news_api= os.getenv("News_api")
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_data=requests.get(url=f"https://newsapi.org/v2/everything?q=tesla&from=2023-03-11&sortBy=publishedAt&language=en&apiKey={news_api}")
for n in range (3):
    title=news_data.json()['articles'][n]['title']
    title_url=news_data.json()['articles'][n]['url']
    message+= f'Title: {title}\nUrl: {title_url}\n\n'
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
print(percentage)
print(message)


my_email="regasir12@gmail.com"
password=os.getenv("email_password")

def email():
    
    print("HH")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=f"{password}")
        connection.sendmail(from_addr=my_email,
                        to_addrs="sujalxetry00@gmail.com",
                        msg=f"Subject:Stoke ALert\n\nTesla {percentage}\n{message}.")
        
        
email()





#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

