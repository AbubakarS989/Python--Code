# Memory View 
# memoryview()
#  return value , how data is represented in the memory
# b for bytes
x=b"helo"
men=memoryview(x)

print(chr(men[1]))

print(bytes(men[1:3]))

 
