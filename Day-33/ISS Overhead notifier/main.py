import requests
from datetime import datetime 
import smtplib

my_email="regasir12@gmail.com"
password="btzyjsfsqwninjhj"

def email():
    print("HH")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                        to_addrs="sujalxetry00@gmail.com",
                        msg=f"Subject:Look Up\n\nThere is ISS above you.\nLook Up.")

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
# print(iss_latitude,iss_longitude)
# print(MY_LAT,MY_LONG)

lat_diff=iss_latitude-MY_LAT
long_diff=iss_longitude-MY_LONG
print(lat_diff,long_diff)
#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunrise,sunset)
time_now = datetime.now()
print(time_now.hour)


if (lat_diff<60 or lat_diff>-60) and (long_diff<60 or long_diff>-60):
    if sunset<=time_now.hour or sunrise>=time_now.hour:
        email()
        



#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
