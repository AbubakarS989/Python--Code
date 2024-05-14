#  We can also rise custom error in our program

num = int(input("Enter a number btw(1-6): "))
try:
    if num>=1 and num<=6:
        print("You are right")
    else:
        raise ValueError
except:
    print("Great Job!!")
finally:
    print("Great Job  Good luck!!")
