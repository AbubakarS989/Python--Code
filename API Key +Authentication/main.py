import requests

#! Weather Website where I get KEY and Weather APi
# https://home.openweathermap.org/api_keys

longitude=70.1307
latitude= 28.3062
# 
API_KEY="00c51655b4896fedab537cc560012f8a"
# ! Sadiqabad weather data 
response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast?lat=28.3062&lon=70.1307&appid=00c51655b4896fedab537cc560012f8a",)


response.raise_for_status()
print(response.json())

