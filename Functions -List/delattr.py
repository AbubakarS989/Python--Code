# Del attribute
# delattr()
# delattr(object name,attribute)
# it is equivalent to :-> del object_name.attribute
# del  myclass.x
class MyClass:
    def __init__(self,x):
        self.x=x


# object
myclass=MyClass(10)
print(myclass.x)
delattr(myclass,"x")
print(myclass.x)

