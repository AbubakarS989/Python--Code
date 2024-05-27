
#! Module provide checking length and strengthens(weak,too weal,medium,strong) of given password


# module-1-pass-day-1
# ! Two type of checker:
# 1. Lengthy
# 2 . One liner
# 3: Combine


# TODO Define the Criteria for a Strong Password:
# Minimum length (e.g., at least 8 characters)
# Contains both uppercase and lowercase letters
# Includes digits
# Has special characters (e.g., !, @, #, $, etc.)

# TODO Create the Function:
# Define a function that takes a password as input.
# Check if the password meets the criteria.
# Return a strength score or a strength classification (e.g., "Weak", "Moderate", "Strong").

# TODOImplement the Function:

# Use regular expressions to check for each criterion.
# Accumulate a score or classify the password based on the number of criteria met.
# from user
print("------------Type 1: Lengthy -----------")
import re  
# re-> expression
# password=input("Enter your password: ")

# test
password = "abU]*89Id98"

# check strengthens


def check_password(password):
    strength_score = 0

    # check length
    if len(password) >= 8:
        strength_score += 1
    else:
        strength_score -= 1
        print("Password is too short, it should be at least 8 characters.")

    # check Uppercase
    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        print("Password Should contain at least 1 Uppercase letter.")
        strength_score -= 1
    # check lowercase
    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        print("Password Should contain at least 1 lowercase letter.")
        strength_score -= 1

    # check number
    if re.search(r'[1-9]', password):
        strength_score += 1
    else:
        print("Password Should contain at least 1 digit letter.")
        strength_score -= 1
    # check symbol
    bracket = [']', '[']
    ''' To check [] these brackets i use list comprehension'''

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password) or [item for item in bracket if item in password]:
        strength_score += 1
    else:
        print("Password Should contain at least 1 special symbol letter.")
        strength_score -= 1

    # print strengthens according to the [strength score]
    if strength_score == 5:
        print("Strong")
    elif strength_score >= 3:
        print("Moderate")
    elif 1 < strength_score < 3:
        print("weak")
    elif strength_score == 1:
        print("Too Weak, Change it to not to be hacked")

    check=re.search(r'[A-Z]', password) 
    # return matching alphabet
    # <re.Match object; span=(2, 3), match='U'>
    print(check)
    # check=[item for item in bracket if item in password ]
    # if check:
    #     print("hi")


# to run fun un commit the below line
# check_password(password)

print("------------Type 2: One liner -----------")

# if len(password) >= 6 and any(char.isdigit() for char in   password)and any(char.isalpha() for char in password) and any(char.islower() and char.isupper() for char in password):
#     print("8")
def one_liner_check(password):
    symbols = '[]!@#$%^&*(),.?"{:|<>'
    if (len(password) >= 6   and  any(char.isdigit() for char in   password) and  any(char.isalpha() for char in password) and  any(char.islower()  for char in password) and (char.isupper()  for char in password) and  any(char in symbols for char in password )):
        print("strong Password")
        
    else:
        print("weak")
        
        
# to run fun un commit the below line
# one_liner_check(password)
print("------------Type 3: Combine -----------")

def combine(password):
    '''This method is not secure as it return true if user input 1 character neither any symbol, or upper lower letter.'''
    # if any of the character matches,  it return true.

    if re.search(r'[1-9,a-z,A-Z,!@#$%^&*(),.?":{}|<>]', password) and len(password)>=8:
        print("hi")
    else:
        print("false")
        

# combine(password)