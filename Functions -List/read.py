# Read
# read()
# Modes of reading a file

# Mode:
# "r"-open for reading(default)
# "w"- open for writing, truncating the file first
# "x" -open for creation, failing if file exist already
# "a" -open for writing, appending to the end of the file if it exist 
# "b" -binary mode 
# "t" -text mode (default)
# "+" open for updating (reading and writing )

f=open("int.py","r")
lines=f.readlines()
print(lines) # return list of data


with open("Max.py","a+") as f:
    f.write("hi")
    

# save json data
import json
# write data
data={"A":"you are strong"}
with open("data.json","w") as f:
    json.dump(data,f)
# load data
with open("data.json","r") as f:
    print(json.load(f))