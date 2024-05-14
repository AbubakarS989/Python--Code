travel_log = []

def add_new_country(country,visit,cities ):
   new_visit={}
   new_visit["country"]=country
   new_visit["visits"]=visit
   new_visit["cities"]=cities
   travel_log.append(new_visit)

#🚨 Do NOT change the code above


#TODO: Write the function that will allow new countries
cont_visit=int(input("How many countries you wanna added"))

for _ in range(cont_visit):
    cities=[]
    country=input("Enter country name you visited :")
    visits=input(f"Enter a number of time you visits to {country} country :")
    visits_city=int(input(f"How many cities you visit :"))
    for _ in range(visits_city): 
        city=input("Enter names of city you travel:")
        cities.append(city)


    add_new_country(country, visits, cities)
print(travel_log)
    

