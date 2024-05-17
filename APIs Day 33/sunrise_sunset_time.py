import requests
from datetime import datetime

# current time
time_now_hour=datetime.now().hour
print(time_now_hour)


# ! SadiqAbad City Pakistan
latitude=28.310350
longitude=70.127403
# tzid="Asia/Karachi"
parameters={
    "lat":latitude,
    "lng":longitude,
    "formatted":1,
    "tzid": "UTC"
    
}

response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data=response.json()
sunrise=data["results"]["sunrise"]
sunset=data["results"]["sunset"]
print(sunrise)
print(sunset)

# take hour value from the entire date time
list_data_R=sunrise.split(":")
list_data_S=sunset.split(":")
print(list_data_R)
print(list_data_S)
API_hour_sunrise=int(list_data_R[1])
# API_hour_sunrise=API_hour_sunrise-24
API_hour_sunset=int(list_data_S[1])
# print(API_hour_sunrise)

if time_now_hour==API_hour_sunrise:
    print("sunrise")
elif time_now_hour== API_hour_sunset:
    print("sunset")
else:
    print("No sunset and no sunrise")
