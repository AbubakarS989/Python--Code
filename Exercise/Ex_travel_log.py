travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country,visit,cities ):

   new_visit={}
   new_visit["country"]=country
   new_visit["visits"]=visit
   new_visit["cities"]=cities
   travel_log.append(new_visit)

#🚨 Do NOT change the code above


#TODO: Write the function that will allow new countries
cities=[]
country=input("Enter country name you visited :")
visits=input(f"Enter a number of time you visits to {country} country :")
visits_city=int(input(f"How many cities you visit :"))
for _ in range(visits_city): 
    city=input("Enter names of city you travel:")
    cities.append(city)


add_new_country(country, visits, cities)
print(travel_log)
    






#🚨 Do not change the code below
# print(travel_log)
