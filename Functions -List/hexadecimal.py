# hexadecimal
# hex()
# It return hexadecimal value of an integer
# For OOps, it apply only for class method __index__
class customClass:
    def __index__(self):
        return 10
    
print(hex(225))
print(hex(1))

c=customClass()

print(hex(c))