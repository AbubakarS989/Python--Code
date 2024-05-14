num=input("Enter a number:")

try:
    for i in range(1,11):
        print(f"{int(num)}X{i}={int(num)*i}")
    list_E=[1,2,455,45,3]
    print(list_E[int(num)]) 

# In except we can control the errors or specified errors and do anything when particular type of error occurred
except ValueError:
    print("Value error")
    print(f"Your input value is \"{num}\" ")

except IndexError:
    print("Index error")

print("We run shamelessly")