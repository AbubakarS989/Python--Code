

class send_data_sheet:
    pass



import requests ,json
# GET DATA FROM SHEET


# ? Access from APi
# r=requests.get(url="https://api.sheety.co/7fdfd106e49f87ee32b27f1188f05994/newMemberData/formResponses1")
# data=r.json()
# print(data)

# with open("raw_data.json","w") as f:
#     json.dump(data,f,indent=4)
    
# # refine the raw data and store as a meaning full names
# length_items=len(data["formResponses1"])


# print(data["formResponses1"][0].keys())
# for index in range(length_items):
#     name=data["formResponses1"][index]["whatIsYourName ?"]
#     print(name)

# ? Access from json

with open("raw_data.json","r") as f:
    raw_data=json.load(f)
    

entire_data=[]

for data in raw_data["formResponses1"]:
    print("-"*50)
    # get date and time
    date,time=  data["timestamp"].split(" ")[0],data["timestamp"].split(" ")[1]
    # print(data)
    # print(time)
    individuals_data={
        "ID":data["id"],
        "Date":date,
        "Time":time,
        "Name":data["whatIsYourName ?"],
        "Age":data["whatIsYourAge?"],
        "Gmail":data["enterYourGmailAddress"],
        "Blood_G":data["enterYourBloodGroup"],
        "Number":data["whatIsYourPhoneNumber? [whatsappPreffered ]"],
        "Jazzcash":data["jazzcashOrNot?"],
        "Experience":data["anyPastExperienceShop?"],
        "Address":data["enterYourHomeAddress:"],
        "Self_Detail":data["anythingYouWannaTellUsAboutYourself?"],    
    }
    entire_data.append(individuals_data)

with open("refine_data_new.json","w") as f:
    json.dump(entire_data,f,indent=4)
    
print(entire_data)