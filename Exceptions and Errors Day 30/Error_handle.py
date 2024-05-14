# File not Found
# w -> if it's not exist it created then!
try:
    file=open("a_file.txt")  # can cause error
    dictionary={"a":"asa"}
    print(dictionary["a"])


except FileNotFoundError as error :  # specify the error 
    file=open("a_file.txt","w") 
    file.write("Helo from txt sdb")
    file.close()

    print(f"The files {error} does't exist")

except KeyError as error_msg:
    print(f"The key {error_msg} does't exist")

else:
    ''' If the TRY run's and no exceptions are occur then program moves to the ELSE block'''

    content=file.read()
    file.close()
    print(content)

finally:
    ''' It doesn't care anyone and run shamelessly hehe'''
    print("Hi i never stop working ")


raise IndexError("where is index error")  
''' We can raise our own Errors using 'raise keyword' '''