# Syntax for list comprehensive
# name="Ali"
# new_list=[letter for letter in name]

# This is simple code for list we use earlier


# list_5=[]
# list_3=[]
# for i in range(100):
#     if i%5==0:
#         list_5.append(i)
#     else:
#         if i%3==0:
#             list_3.append(i)      
# print(list_5)
# print(list_3)

# List Comprehensive
list_3=[i for i in range(100) if i%3==0 ]
list_5=[i for i in range(100) if i%5==0]
print(list_5)
print(list_3)


# dic Comprehensive
# key value pairs

dic1={i:f"item{i}" for i in range(100) if i%10==0 }
# now reverse the dic
dic2={value:key for key , value in dic1.items()}
print(dic2) 

# set comprehension

dresses= {dress for dress in ["d1","d2","d1","d2","d1"]}
print(dresses)



name="abubakar"
# add string into list
name_list=[i for i in name]
# output
# ['a', 'b', 'u', 'b', 'a', 'k', 'a', 'r']
print(name_list)

number=[1,2,3]
number=[i+1 for i in number ]
print(number)

ran=[i*2 for i in range(1,5)]
print(ran)

# Exercise   
list_name=["ali","ahmad","usman","dowaed"]
upper_name=[name.upper() for name in list_name ]
list_name=[name for name in list_name if len(name)==6]
print(list_name)
print(upper_name)


# Exercise   
integers=[1,1,2,3,5,8,13,21,34,55]
square=[num*num for num in integers]
even=[num for num in integers if num%2==0 ]
print(square)
print(even)

# with open("data.csv","r") as f:
#     line=f.readline()
#     print(line.strip())


# practice

# store num to new list if both list have common numbers

list1=[1,2,3,4,5]
list2=[1,2,8,4,6]
new_list=[i for i in list1 if i in list2]
print(new_list)
    
