

# ! MY Code
# import re
# ''' It check the validation of gmail'''

# gmail="abcA8y@gmail.com".strip() #remove space from left and right

# def check_Gmail_module(Email):
    
#     '''Each email  must contain 1 @ symbol and 1 . dot'''
    
#     # set strengthens
#     strength=0
#     # check @
#     if '@' in Email :
#         strength+=1
#         # check .
#         if '.' in Email:
#             strength+=1    
#             # check .   digits and alphabets
#             if re.search(r'[a-zA-Z0-9]',Email):
#                 strength+=1
#                 # check .   special symbols
#                 if not  re.search(r'[!#$%^&*(),?":{}|<>]',Email):
#                     strength+=1
#                 else:
#                     print("Invalid, Special Symbol are not allowed else '@' and '.'")
#             else:
#                 print("Invalid,Email Should Contain at least one number.")
#         else:
#             print("Invalid,Email Should contain '.' symbol")
#     else:
#         print("Invalid,Email Should contain '@' symbol ")
    
#     # check length of an Email
#     # Minimum -> 6 
#     # Maximum -> 30
#     # First we need to get the first characters until '@' this sign
#     start_character= gmail.split('@')[0] 
        
#     # start character Mean:
#                     #The first part of gmail until '@'

#     print(start_character)
    
#     # We get starting character:now check the length min:6,max,30
#     if len(start_character)>=6 and len(start_character)<=30:
#         strength+=1
#     elif len(start_character)<6:
#         strength-=1
        
    
#     # Return State. acc. to strength
#     if strength==5:
#         print("Secure Email.")
#     elif strength==4:
#         print("Email should not less than 6 Character.Make it Secure")
#     print(strength)

#     return strength

# check_Gmail_module(gmail)    



# ! Code With Try and Error Handling

import re

Gmail="abubakarhafeez66@gmail.com"

def check_email_secure(gmail):
    
    if not "@" in gmail:
        raise ValueError("Invalid Email. '@' is missing")
    
    if not "." in gmail:
        raise ValueError("Invalid Email. Dot '.' is missing")
    
    if  not re.search(r'[1-9]',gmail) :
        raise ValueError("Email should contain at least one Number. ")
    
    if re.search(r'[!#$%^&*(),?":{}|<>]',gmail) :
        raise ValueError("Invalid Email. Special symbols are not allowed. ")
    
    # get start character of gmail until @
    email_char=gmail.split("@")[0]
    
    print(email_char)
    
    if  not any(char.isalpha() for char in email_char):
        raise ValueError("Email must contain  alphabet character (a-zA-Z).")
    # Min-> 6
    # Max-> 30
    if not 6<=len(email_char)<=30 and len(email_char)==0:
        raise ValueError("Invalid Email.Gmail ID length should be between 6 and 30 characters ")
    
    
    return "-secure Email.Thank You"
        
        
try:
    print(check_email_secure(Gmail))
except ValueError as e:
    print(f"- {e}")   
    print("- Please Re-Check Your Email.Thank You")