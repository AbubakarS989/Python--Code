import os

#? Open the file in write-only mode
#? Open the file in read-only mode


#? Open the file in read-only mode
f = os.open("myfile.txt", os.O_RDONLY)

# Read the contents of the file
contents = os.read(f, 1024)

# Close the file
os.close(f)


#? Open the file in write-only mode
f = os.open("myfile.txt", os.O_WRONLY)

# Write to the file
os.write(f, b"Hello, world!\nHi")

# Close the file
print(contents)
os.close(f)