# Get Attribute
# getattr()
# The getattr() function in Python is used to retrieve the value of an attribute from an object. If the attribute doesn't exist, you can provide a default value to be returned instead of raising an AttributeError.

class myClass:
    def __init__(self,x):
        self.x=x
        


y=myClass(10)

print(getattr(y,"x"))