
from twilio.rest import Client
import os
import requests


# Set environment variables (for testing purposes only)
# os.environ['TWILIO_ACCOUNT_SID'] = 'AC3bec8567c443a97e6fd714945e9fec8a'
# os.environ['TWILIO_AUTH_TOKEN'] = 'ebf32485f7d16ac2c30b9e9943a4b9c7'
# API_KEY = "00c51655b4896fedab537cc560012f8a"
latitude = 28.310350
longitude = 70.127403
# cnt -> number of times we need data in each day
parameters = {
    "lat": latitude,
    "lon": longitude,  # Corrected parameter from "lng" to "lon"
    "appid": API_KEY,
    "cnt": 4,
}
# https://openweathermap.org/weather-conditions
# https://api.openweathermap.org/data/2.5/forecast?lat=28.3062&lon=70.1307&&cnt=4&appid=00c51655b4896fedab537cc560012f8a

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast?lat=28.3062&lon=70.1307&&cnt=4&appid=00c51655b4896fedab537cc560012f8a")
response.raise_for_status()
# first_weather_list=response.json()["list"][0]['weather']
# first_id=first_weather_list[0]["id"]

# second_weather_list=response.json()["list"][1]['weather']
# second_id=second_weather_list[0]["id"]
# print(first_id)
# print(second_id)
[{ 'id': 800,
   'main': 'Clear',
   'description': 'clear sky',
   'icon': '01d'}
 ]

# create a loop that get id from each weather list and append it into a list of ids
ids_list=[]
for i in range(4):
    multi_list=response.json()["list"][i]['weather']
    id=multi_list[0]["id"]
    ids_list.append(id)


print(ids_list)    
# if any condition code(id) is less than 700 bring an Umbrella

# Group 80x: Clouds
# 801	Clouds	few clouds: 11-25%	 
# 802	Clouds	scattered clouds: 25-50%	 
# 803	Clouds	broken clouds: 51-84%	
# 804	Clouds	overcast clouds: 85-100%	 

# Msg setup
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
# set TWILIO_ACCOUNT_SID='AC3bec8567c443a97e6fd714945e9fec8a'
# set TWILIO_AUTH_TOKEN='ebf32485f7d16ac2c30b9e9943a4b9c7'
if any(id >= 800 for id in ids_list):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_='+16364518304',
    body="No umbrella needed",
    to='+923187764396'
    )
    print("No umbrella needed")
    print(message.status)
    
elif any(id >=700  for id in ids_list):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_='+16364518304',
    body="Bring an Umbrella ",
    to='+923187764396'
    )
    print("Bring an Umbrella")
    print(message.status)
    
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# set up twilio client 


