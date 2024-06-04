# Has attribute
# hasattr()
# This check if any attribute is available in the object or not


class myclass:
    def __init__(self,x):
        self.x=x
        
c=myclass(10)

print(hasattr(c,"x"))
# x is defined in C so it return TRUE
print(hasattr(c,"y"))
# y is not defined in C so it return False

