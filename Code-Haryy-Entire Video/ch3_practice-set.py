# CHAPTER 3 – PRACTICE SET


# TODO 1. Write a python program to display a user entered name followed by Good Afternoon using input () function.

# name=input("Enter your name:")
# print(f"Good Afternoon {name}!")

# TODO 2. Write a program to fill in a letter template given below with name and date.
import datetime
current_dat=datetime.datetime.now().date().strftime("%Y-%m-%d") #change date into string format 
print(type(current_dat))
name=input("Enter your name: ")
letter = f'''
      Dear <|Name|>,
      You are selected!
      <|Date|>
''' 
print(letter.replace("<|Name|>",name).replace("<|Date|>",current_dat))
# TODO 3. Write a program to detect double space in a string.

statement="helo what are u doing today? can we  meet?"
print(statement.index("  "))

# TODO 4. Replace the double space from problem 3 with single spaces.
print(statement.replace("  "," "))

# TODO 5. Write a program to format the following letter using escape sequence
# characters.
letter = "Dear Harry,\n\tthis python course is nice.\nThanks!"
print(letter.title())