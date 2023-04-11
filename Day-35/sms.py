import os
from dotenv import load_dotenv

from twilio.rest import Client
load_dotenv("D:/SAT/ss/Documents/docs/EnvironmentVariable/.env")

auth_token=os.getenv("twilio_token")
acc_sid="ACccb9465d5d4237b0a158ac14826fb231"


client= Client(acc_sid, auth_token)
message = client.messages \
                .create(
                     body="Hello KX",
                     from_='+15076876682',
                     to='+9779824162576'
                 )
    
print(message.status)