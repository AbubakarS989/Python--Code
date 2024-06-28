
#? List Method
#1:  sort(): updates the list to [1,2,7,8,15,21]
#    sort(key=None, reverse=False):
#2:  reverse(): updates the list to [15,21,2,7,8,1]
#3:  append(8): adds 8 at the end of the list
#4:  insert(3,8): This will add 8 at 3 index
#5:  pop(2): Will delete element at index 2 and return its value.
#6:  remove(21): Will remove 21 from the list.
#7:  extend([4, 5])  # lst becomes [1, 2, 3, 4, 5]
#8:  clear() Remove all items from the lis
#9:  count() -Count the specific item in list
#10: copy() -Returns a shallow copy of the list
#11: use of [in] keyword to check something is present or not, in list

#TODO Add an item at the end of list.
data=["ahmad",45,89.34,"A",True,5>2]
data.append("ali")
print(data)


#TODO Sort the list into numeric order
num_list=[23,2,456,45,90,1,12]
num_list.sort()
print(num_list)

#TODO Reverse the list 
num=[9,8,7,6,5,4,3,2,1]
num.reverse()
print(num)

#TODO Insert something at specific index
data=["ahmad",45,89.34,"A",True,5>2]
data.insert(1,"Yaqoub") #([index num],[value])
print(data)

#TODO delete item from specific index and get the value also
print(data.pop(2))
print(data)

#TODO Extend the list with extra items
# add item at the end
data.extend(["abubakar","ALi"])
print(data)


#TODO remove item from specific index permanently

data.remove("ahmad")
print(data)

# TODO count the specific item in the list
print(data.count("ALi"))

# TODO remove all items
lst=[2,34,4]
lst.clear()
print(lst)


# TODO create copy of list
print(data.copy())


# TODO check something is present or not
print("ALI" in data)
