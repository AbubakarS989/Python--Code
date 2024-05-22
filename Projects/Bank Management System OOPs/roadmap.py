
#! Key features
# User add --> dic
# id --assign by me
# name
# gmail
# pss
# pin
# gen code send to the user gmail and then match the code
# TODO the above part is done
# User Remove
# need to login to account:
# gen code send to the user gmail and then match the code
# id
# pin code-

# Withdraw money
# Add mOney
# send money
# check balance
# get loan
# send money as charity
# get record

# TODO All actions are made through account id and pin code
# if pin is not available then password



# ! my logic
#! logic for gene id and assign it user uniquely
# import random
# random_value=[]
# for _ in range(len(random_value)+1):
#     value=random.randint(1,100)
#     if value not in  random_value:
#         random_value.append(value)
#     else:
#         value=random.randint(1,100)

# print(random_value)
import random
dic = {"id": {"name": "ali","pass": "asv","PIN": 3445 ,"gmail": "@gmail.com" }
}


# id_list_assign=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 
# 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 
# 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 
# 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 
# 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 
# 98, 99, 100]
# value={ "name": "ali",
#     "pass": "asv",
#     "PIN": 3445,
#     "gmail": "@gmail.com"}
# di={
#     1:value
# }
# if id not in di:
#     id=random.choices(id_list_assign)
# print(id)

# print(f"This is your ID save it, ID will be  use to access, edit and for every transaction you made.! Don't forget it\nID :{i} ")
import random

id_list_assign = [i for i in range(1, 101)]  # Creating a list of IDs from 1 to 100

value = {
    "name": "ali",
    "pass": "asv",
    "PIN": 3445,
    "gmail": "@gmail.com"
}

di = {
    1: value  # Example entry in the dictionary, replace with your actual entries
}

if id not in di:
    id = random.choice(id_list_assign)  # Selecting a random ID from the list

print("Generated ID:", id)
print("This is your ID. Save it, as it will be used to access, edit, and for every transaction you make!")

value = {
    "name": "ali",
    "pass": "asv",
    "PIN": 3445,
    "gmail": "@gmail.com"
}
di[id]=value
print(di)

# if id not in di:
#     di[id]="no"
# else:


#! comp logic
# import random

# random_value = []

# # Generate 10 unique random integers
# while len(random_value) < 10:
#     value = random.randint(1, 100)
#     if value not in random_value:
#         random_value.append(value)

# print(random_value)