# Strings are immutable-can't change
# right side of value is not include while slicing 
# Three ways to write string
name1='Abubakar'
name2="Abubakar"
name3=""" Abubakar"""

#Slicing of string 
nm="Ahmad"
shortname=nm[0:4] #start from index 0 to index 3 but 4 is excluding
print(shortname)


name="How are you?"
shortname=name[1:11] # positive indexing 
print(shortname)    
shortname=name[-11:-1] # negative indexing
print(shortname)    

# Negative to positive
# Working of -ev indexing 
# a b u b a k a r
# 0 1 2 3 4 5 6 7
#-8-7-6-5-4-3-2-1
name="abubakar"
print(name[-5:-3]) #start exclude(3 not include)
print(name[3:5])


# If start value is empty
name='eman'
print(name[:2]) # is same as name[0:2]- empty represent "0"

# If end value is empty
name='eman'
print(name[1:])#is same as name[1:len-1] - empty represent end character 


# Slicing with skip value
# First, cut the string, then skip the characters
num="0123456789"
skip_value=num[1:10:2]
# Step1: [1:10]
# 123456789
# Step 2: [1:10:2]
# Skip values with 2 -> 2-1=1
# 1 3 5 7 9
print(skip_value)