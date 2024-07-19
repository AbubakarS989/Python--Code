

import os
import shutil



# ? List of modules
# 1: mkdir([folder name])  - Create new folder
# 1: mkdirs([folder name])  - Create new folder and sub folders 
# 2: rmdir([folder name/Sub folder]) - Remove sub folder
# 3: os.rename([Folder or file name]) -change the name
# 4: os.path.exists([Folder or file name]) -check exist file
# 5: os.listdir([Folder name]) -get the list of all files present in the directory
# 6: os.getcwd() - check the current directory
# 7: os.remove(path) 
# 8: os.rmdir(path) -del the empty directory
# 9: shutil.rmtree() - del all file in the directory
# [shutil module must be import first]
# 10:  os.open("path", os.O_RDONLY)
# 11: os.open("path", os.O_WRONLY)
# 12: os.environ.get("Path") - get all env variables
#13: os.path.join(path,file) - join the file to path optimal way
# isfile
# isdir





#? Create  folder
# os.mkdir("dummy")
open("environment-var-os.py","w")
#? Rename the Specific file or folder
# os.rename("Change-File-name.py","list-os-fun.py")

#? check the specific file and folder exist or not
if os.path.exists("list-os-fun.py"):
    print("It Exist")
    
# ? Remove the sub folder or file
# Folder:  os.rmdir("Folder\Folder 2")
# File :   os.rmdir("Dummy.py")

# ? GEt the list of files present in the specific folder
# print(os.listdir("Folder"))

# ? If we have to create number of folders 
# for i in range(3,101):
#     os.rename(f"Folder/Folder {i}",f"Folder/Day {i}")

#? IF we want to get the list of items in all sub folder of a folder then:
folders=os.listdir("Folder") 

# we check each folder and make it a list 
for folder in folders:
    print(f"{os.listdir(f"Folder/{folder}")}")

# ? Current directory name
print(os.getcwd())

#? Remove all file of the directory
# shutil.rmtree("D:\Dummoy")

# ? join path
print(os.path.join("d:","myfile.txt"))

print(os.path.isdir("d:"))
print(os.path.isfile("myfile.txt"))
