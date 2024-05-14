Texts= "This is written in file handling  and open in text.txt file"

# open() we can open amy file
#  close is used when we don't use (with) keyword
fp=open("Create_with_me.py", "w")
fp.close()

# here we create new file Creat_with_me.py with write mode (w)
with open("Creat_with_me.py", "w") as f:
    f.write(Texts)