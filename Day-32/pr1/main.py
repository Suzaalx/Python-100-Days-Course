import smtplib
import datetime as dt
import random

my_email="regasir12@gmail.com"
password="NO"
def email():
    quotes=open("Day-32/quotes.txt").read().splitlines()
    quote=random.choice(quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                        to_addrs="sujalxetry00@gmail.com",
                        msg=f"Subject:Motivational quote\n\n{quote}")
    
    



now=dt.datetime.now()
print(now.weekday())
if now.weekday()==1:
    email()