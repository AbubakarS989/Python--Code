
#TODO List of methods
#1: items(): Returns a list of (key,value)tuples.
#2: keys(): Returns a list containing dictionary's keys.
#3: update({key:value}): Updates the dictionary with supplied key-value pairs.
#4: get("name"): Returns the value of the specified keys (and value is returned
# eg."harry" is returned here).
# 5: values()
# 6: pop()
# 7: popitem()
# 8: clear()
# operations
# 9: Deleting a Key-Value Pair:
# 10: Adding/Updating Values:
# 11: dictionary with initial key-value pairs 
# 12: Accessing Values
marks={
    "Ali":45,
    "ahmad":98,
    "ahsan":12
    
}
#? get the total items with keys
print(marks.items())

#? Get all keys
print(marks.keys())

#? add item into dic
marks.update({"abdullah":67})
print(marks)

#? get the specific item value
print(marks.get("abdullah"))

#? get all values
print(marks.values())

#? remove specific item and return that value 
print(marks.pop("Ali"))
print(marks)

#? dict.popitem(): return last value pair
# Removes and returns a key-value pair from the dictionary. Pairs are returned in LIFO (last-in, first-out) order.
print(marks.popitem())

#? dict.setdefault(key, default=None):
# If key is in the dictionary, return its value. If not, insert key with a value of default and return default.
print(marks.setdefault("Ali",89))
print(marks)

#? Operation on dic
d = {}  # empty dictionary
d = {'a': 1, 'b': 2}  # dictionary with initial key-value pairs
print(d)

#? Accessing Values
d = {'a': 1, 'b': 2}
value = d['a']  # returns 1
print(value)

#? Adding/Updating Values:
d = {'a': 1}
d['b'] = 2  # adds a new key-value pair, d is {'a': 1, 'b': 2}
d['a'] = 3  # updates an existing key, d is {'a': 3, 'b': 2}
print(d)

#? Deleting a Key-Value Pair:
d = {'a': 1, 'b': 2}
del d['a']  # d is now {'b': 2}
print(d)
