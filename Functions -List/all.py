# ALL ->iterable
# all()
# Return True if all element of the iterable are true 
# Return False if iterable is empty 

a=[]
print(all(a)) #-> True 

b=[0,1,2,3,4]
print(all(b))

c=[True,False,1,2]
print(all(c))

d=[[0,0],[0,0],[0,0]]
print(all(d)) #True: bcz outer list is not empty 

e=[[],[1],[True]]
print(all(e))  #False: bcz one inner list is empty thats why return false




