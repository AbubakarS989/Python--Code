
dic={

    "name":"Abubakar",
    "class":"19"
}


#  Method of dictionary 
print(dic["name"])
print(dic["class"])
print(dic.keys())
print(dic.values())
print(dic.get("a")) # return none instead of an error
print(dic.items())
# print(dic["na"]) return error in case nothing find

dictionary={}
while True:
    user_input = input("Enter key-value pair (or 'done' to finish): ")
    if user_input == "done":
        break

    key, value = user_input.split(":")
    dictionary[key] = value




for i in dictionary:

    print(f"{i}  {dictionary[i]}:")


# print(dictionary)
