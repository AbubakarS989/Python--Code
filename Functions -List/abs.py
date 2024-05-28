# Absolute Value
# abs()
# convert -ev value to +ev:
class Implement_Abs():
    def __init__(self,string):
        self.string=string
    
    def __abs__(self):
        return self.string.lower()
    
    
    
statement=Implement_Abs("HELLO")
print(statement.__abs__())
x=abs(-93.3)
y=abs(-23)
z=abs(statement)

# output
print(x)
print(y)
print(z)

