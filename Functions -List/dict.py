# Dictionary
# dict()
# to create a new dictionary

# Format


my_list=[("a",1),("b",2)]
my_dict=dict(my_list)
print(my_dict)
# output
# {
# 'a': 1,
# 'b': 2
#  }

# take input from the user


my_list=[]
for _ in range(2):
    key=input("Enter a key")
    value=int(input("Enter a value"))
    my_list.append([key,value])
    
print(my_list)    
    
my_dict=dict(my_list)
print(my_dict)
# output
# {
# 'a': 1,
# 'b': 2
#  }


