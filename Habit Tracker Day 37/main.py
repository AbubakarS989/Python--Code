import requests




# post - upload new data
# put - update the existing data
# pull - get the data
# delete - delete the data

print("------------- Welcome to Habit Tracker -------------------\n")
USER_NAME=input("Enter your Username : \n")
TOKEN=input("Enter your Token : \n")
print("------------- Select one of them -------------------\n")
print("""
    1: Add your today Track.
    2: Update your particular Track.
    3: Delete your particular Track.
    4: Show your particular Track Value
        """)
    




# ! For Token and Username visit folder 
# - D:\Endpoints
# ? Step 1: To create user account 
# url endpoint
pixela_endpoint="https://pixe.la/v1/users"
user_params={    
"token":TOKEN,
"username":USER_NAME,
"agreeTermsOfService":"yes",
"notMinor":"yes",
}
# uncomment, to create a new account 
# r=requests.post(url=pixela_endpoint,json=user_params)
# print(r.text)
# account is created at pixela


# ? Step 2: Create new graph 
graph_id="bkrgraph1"
graph_params={
    "id":graph_id,
    "name": "Code Tracker Graph",
    "unit":"h",
    "type":"float",
    "color":"shibafu" # green
    
}
header={
    "X-USER-TOKEN":TOKEN
}

# get entire track:
pixels_paras={
            "from":"20240714",
            "to":"20240719",
            "withBody":True
        }
get_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{graph_id}/pixels"
r = requests.get(url=get_endpoint,params=pixels_paras, headers=header)
r.raise_for_status()
qty=r.json()
print(qty)
# endpoint for to check graph
graph_endpoint=f"{pixela_endpoint}/{USER_NAME}/graphs"
# r=requests.post(url=graph_endpoint,json=graph_params,headers=header)
# print(r.text)

# ? Step 3: Upload your data to graph
from datetime import datetime

current_date=datetime.now().date().strftime("%Y%m%d")
# print(current_date)
data_param={
    "date":current_date,
    "quantity":input("How many hours did you work today?")
    # "quantity":"3.4",
    }

# ? This is for new value

# new data endpoint
data_endpoint=f"{pixela_endpoint}/{USER_NAME}/graphs/{graph_id}"
# r=requests.post(url=data_endpoint,json=data_param,headers=header)
# print(r.text)
# want to update the value then we use [put method]

# ? This is for to update the existing value
update_value={
 "quantity": "7.30"  
}
# Uncomment , to get the manual data
manual_date=datetime(year=2024,month=7,day=14).strftime("%Y%m%d")

# new endpoint for updating existing values

update_endpoint=f"{pixela_endpoint}/{USER_NAME}/graphs/{graph_id}/{manual_date}"
# r=requests.put(url=update_endpoint,json=update_value,headers=header,)


# ? This for to get the data from the your graph

# new endpoint for getting data
# v1/users/<username>/graphs/<graphID>/<yyyyMMdd> -FORMAT
get_endpoint=f"{pixela_endpoint}/{USER_NAME}/graphs/{graph_id}/{manual_date}"

# r=requests.get(url=get_endpoint,headers=header)
# print(r.raise_for_status())
# print(r.text) # {"quantity":"0.30"}

#? This for to delete the particular data from the your graph

# new endpoint for deleting data fro graph
# the parameters are same as getting data api
del_endpoint=f"{pixela_endpoint}/{USER_NAME}/graphs/{graph_id}/{manual_date}"

# r=requests.delete(url=del_endpoint,headers=header)
# print(r.text) 


