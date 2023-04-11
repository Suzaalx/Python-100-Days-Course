
from twilio.rest import Client

auth_token="f947f313ae8a88d20f6ae336e5d99fe4"
acc_sid="ACccb9465d5d4237b0a158ac14826fb231"


client= Client(acc_sid, auth_token)
message = client.messages \
                .create(
                     body="Hello KX",
                     from_='+15076876682',
                     to='+9779824162576'
                 )
    
print(message.status)