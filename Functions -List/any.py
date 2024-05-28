# Any
# any()
# Return True if any of the value is true, 
# Return False if all the values are false


a=[True,False]
print(any(a)) #-> True

b=[1,0,223,]
print(any(b)) #-> True

c=[[],[],[]]
print(any(c)) #-> False

d=[[0,0],[0,0],[0,0]]
print(any(d)) #->True

e=[[],0,False]
print(any(e)) #-> False

f=[[],[0],[False]]
print(any(f)) #-> True
