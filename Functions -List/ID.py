#ID 
# id()
# The id() function in Python is used to get the unique identifier of an object. This identifier is unique and constant for the object during its lifetime. It typically represents the object's memory address.

a=[23,4,5,5]
b=a=[2]

c=3+45
d=c+2
print(id(a))
print(id(b))
print(id(c))
print(id(d))
# 2730001488128
# 2730001488128
# 140728866185112
# 140728866185176