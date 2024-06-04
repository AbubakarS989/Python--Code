# Frozen Set
# frozenset()
# immutable, can be use as key for dictionary
lst=[3,45,56]

lst.append(34)
print(lst)

fs=frozenset(lst)
print(fs)
# frozenset({56, 34, 3, 45})


print(34 in fs)  # Output: True

for item in fs:
    print(item)
# Output:
# 3
# 34
# 45
# 56


# Set operations:
fs2 = frozenset([56, 78, 90])

# Union
print(fs.union(fs2))  
# Output: frozenset({3, 34, 45, 56, 78, 90})

# Intersection :value that are present in both set
print(fs.intersection(fs2))  
# Output: frozenset({56})

# Difference
# all elements that are in this set but not the others
print(fs.difference(fs2))  
# Output: frozenset({3, 34, 45})

# Symmetric Difference
#  all elements that are in exactly one of the sets
print(fs.symmetric_difference(fs2))  
# Output: frozenset({3, 34, 45, 78, 90})


# Check if one frozenset is a subset or superset of another:
print(fs.issubset({3, 34, 45, 56, 78}))  # Output: True
print(fs.issuperset({3, 34}))           # Output: True



