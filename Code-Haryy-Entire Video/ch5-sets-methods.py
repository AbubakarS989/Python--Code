
#! Set  methods in python

# 1: add([value])-add value to a set
# 2: len() -check len of set
# 3: remove([value])- remove [value] 
# 4: pop() - remove random value from the set and print that value as well
# 5: clear() -empty the set
# 6: s1.union([s2]) - join both and return new set
# 7: s1.intersection([s2]) - return new set that contain the same values present in both sets
# 8: s1.difference()- return values that are present in s1 not in s2
# 9: s1-s2= value that remain and is not in s2 
# 10: issubset()- if {3,2} are present in s1 then {3,2} are the subset of s1
# 11: discard([value])- remove specific value
# 12: symmetric difference - return value that either in sets but not in both
# 13: superset()- check all elements of s2 are in s1 if any item of them are not present in s1 return false
# 14: isdisjoint()- check no item are same in both sets if both sets are diff return true if each item are same in both sets return false
#! Properties of Set
# Element's ordered does'nt matter
# Cannot access element using index
# We can't change the existing values of set
# Sets can't contain duplicate values

S={3,34,"Hi"}


#? add()
S.add("Code with me")
print(S,type(S))

#? len()
print(len(S))

# ? remove()
S.remove(3)
print(S) 


# ?pop()
print(S.pop())

# ? union()
s1={1,3,5,4,6}
s2={2,4,6,1,2}
print(s1.union(s2))

# ? intersection()
s3={45,67,78,4}
s4={45,76,2,3445,2,4}
print(s3.intersection(s4)) #4,45 value present in both sets
# ? difference()
print(s3.difference(s4)) #67,78 are the values that is not present in s4

# ? s1-s2
print(s1-s2)

# ? subset()
s5={12,1,2,45,8}
s6={12,3}
print(s5.issubset([8,9]))

# ? discard
s6.discard(3) #   3 is removed
print(s6) #1,2 remains


# ? symmetric difference
print(s5.symmetric_difference(s6))

#! Supper set The issuperset method checks if the set is a superset of another set. A set A is considered a superset of set B if all elements of B are also elements of A.
#? Defining sets
set_a = {1, 2, 3, 4, 5}
set_b = {2, 3, 4}

#? Check if set_a is a superset of set_b
is_superset = set_a.issuperset(set_b)
print(is_superset)  # Output: True

#? Check if set_b is a superset of set_a
is_superset = set_b.issuperset(set_a)
print(is_superset)  # Output: False

#! isdisjoint The isdisjoint method checks if two sets have no elements in common. It returns True if they are disjoint, and False otherwise.
#? Defining sets
set_a = {1, 2, 3}
set_b = {4, 5, 6}

#? Check if set_a and set_b are disjoint
is_disjoint = set_a.isdisjoint(set_b)
print(is_disjoint)  # Output: True

# Defining another set
set_c = {3, 4, 5}

#? Check if set_a and set_c are disjoint
is_disjoint = set_a.isdisjoint(set_c)
print(is_disjoint)  # Output: False
