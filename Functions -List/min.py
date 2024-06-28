# Minimum
# min()


lst=[34,454,3,2]
print(min(lst))

print(min(34,-34,434,9))

# return value depend on the first index of list
print(min([2,34,65],[0,343,8]))

print(min("hi","helo","how","why"))


class custom:
    def __init__(self,val):
        self.val=val
        
c1=custom(1)
c2=custom(2)
c3=custom(3)
print(min(c1,c2,c3,key=lambda x:x.val))

