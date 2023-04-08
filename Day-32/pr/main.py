import pandas
import datetime as dt
import smtplib
import random

my_email="regasir12@gmail.com"
password="NO"


data=pandas.read_csv("birthdays.csv")
birthdays=data.to_dict()
email=data["email"]
name=data["name"]
days=data['day'].to_list()

num=0
def birthday(num):
    receiver=email[num]
    
    person=name[num]
    n=random.randint(1,3)
    letter=open(f"letter_templates/letter_{n}.txt").read()
    new_letter=letter.replace("[NAME]", f"{person}")
    
    print(letter)
    print(new_letter)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                        to_addrs=f"{receiver}",
                        msg=f"Subject:Happy birthday\n\n{new_letter}")


for i in range(len(days)):
    now=dt.datetime.now()
    if days[i]==now.day:
        print("Birthday")
        birthday(i)
    






