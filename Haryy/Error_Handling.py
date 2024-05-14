#  Error handling in python

a=input("Enter a number :")

try:
    for i in range(1,11):
        print(f"The table of {int(a)} is :{int(a)*i}")
# except Exception as e:
# except ValueError as e :
except  :
    print("Invalid Input.")

finally: # this will always exe within function after return keyword
    print("I will never stop to print ")

#  Our program will stop here if the use input wrong type of data 
# To overcome this , we use exceptional handling 
print("Some lines of code")
print("ENd of program")
