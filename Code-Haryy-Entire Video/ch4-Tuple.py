 
#! Tuples are immutable, can't change their contents

#? Tuple
tup=(3,"Hi",4.3,4,56,4)
print(tup)

#? create a tuple with one item
tup4=(1,)
print(type(tup4))
# we can't change items
# tup4[0]=2
# print(tup4)

#? There are some methods for tuple 
# 1: count()
# 2: index()
# 3: Accessing elements 
# 4: Slicing
# 5: Concatenation
# 6: Repetition *x
# 7: Membership:
# 8: Unpacking


#TODO count specific item found in list
print(tup.count(4))

#TODO find the index of an item
print(tup.index("Hi"))


# ! Common Tuple Operations


# 3: Accessing elements 
print(tup[2])

# 4: Slicing
print(tup[1:3])

# 5: Concatenation
tup1=(1,3)
tup2=(2,4)
print(tup1+tup2)

# 6: Repetition*x
print(tup*2)

# 7: Membership:
# You can check if an item is in a tuple using the in operator.
print(3 in tup)

# 8: Unpacking
# You can unpack the elements of a tuple into variables.

tup3=(1,2,3)
a,b,c=tup3 # a=1,b=2,c=3
print(a,b,c)

