
# Here is the list of string functions that we can use to get better result:

#1:  len()           -[variable]
#2:  endswith()      -["value"]
#3:  startswith()    -["value"]
#4:  capitalize()    -[capital the string first letter]
#5:  find()          -["value"]  
#6:  replace()       -[new word, old word to replace with]
#7:  upper()         -[uppercase the entire string]
#8:  lower()         -[lowercase the entire string] 
#9:  title()         -[Capitalizes the first character of each word in the string.
#10: strip()         -[Removes leading and trailing whitespace.] 
#11: rstrip()        -[Removes trailing(end) whitespace.]  
#12: lstrip()        -[Removes leading(start) whitespace.]
#13: split()         -["separator"]
#14: join()          - "".join([value1,value2])
#15: index()         -[value] -find index of specify word
#16: count()         -[value] to count
#17: isdigit()       -[check digit present]
#18: isalpha()       -[check char present]
#19: isalnum()       -[check digit and char present] not special char
#20: swapcase()      -[Swaps the case of all characters in the string]
#21: zfill()          -[Pads the string with zeros on the left to fill the specified width.] 

#TODO To check length of string 
value='how are u?' # it count the space btw text
print(len(value))


#TODO To check if particular character is present at the end of a string or not. 
# Return True of False 
# it deals lower or upper separately 
value='ahmad'
print(value.endswith("d")) # True -d is the last char
print(value.endswith("a")) # False - a is not the last char

#TODO To check if particular character is present at the start of a string or not. 
# Return True of False 
# it deals lower or upper separately 
value='ahmad'
print(value.startswith("a")) # True -d is starting char
print(value.startswith("h")) # False - a is not the starting char


# TODO to capital the whole first character into uppercase

value='ali'
print(value.capitalize())



# TODO to find the specific [word or character] in the string
# Return the index of that word 
value="helo how are u?"
print(value.find("a"))


# TODO to replace any word in the string 
value="we need to have.."
chan_value=value.replace("have","change")
print(chan_value) #we need to change..


# TODO split the string with any separator
# Splits the string into a list using the specified separator. If no separator is specified, splits by whitespace.
value="hi how are you? hope you are fine!"
print(value.split(" "))


# TODO join the string with particular values
value1="hi"
value2="abubakar"

print("! ".join([value1,value2])) # hi! abubakar
print("! ".join(["helo","world"])) # helo! world


# TODO find the specified index of a word in a string
# Returns the lowest index in the string where the substring is found. Raises a ValueError if the substring is not found.

value="are u okay?"

print(value.index("?")) # "?" is present at 10 index
# ?
# TODO count the specific  [word or character] occurs in the entire string
# Returns the number of non-overlapping occurrences of a substring.
value="hi buddy, what are you doing?"
print(value.count("are"))
print(value.count("d"))


# TODO check a string contain only alphabets or digits else special symbols, present or not 
value="pass989"
print(value.isalnum())


# TODO to convert the entire lowercase string into uppercase  and uppercase string into lowercase
# Swaps the case of all characters in the string
value="helo world"
print(value.swapcase())


# TODO fill zero at the left side

num="34"
value='ahmad'
print(num.zfill(3))
print(value.isalpha())