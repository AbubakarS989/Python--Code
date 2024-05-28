

#! Functions
# 1: Just split string
# 2: Split from staring point to ending point



#TODO 1: Just split string
# It split the string into 2 parts and store as a list
string='helo@gmail.com'
new_string = string.split('@') 
# print(new_string)


# TODO 2: Split from staring point to ending point
# This method finds the position of the specific letter and the period, and then constructs a new string excluding the specified range.
def remove_from_letter_to_dot(string, letter):
    start_index = string.find(letter)
    end_index = string.find('.', start_index)
    
    if start_index != -1 and end_index != -1:
        string = string[:start_index] + string[end_index+1:]
    return string

# Example usage:
original_string = "This is a sample text, remove from s to . in this sentence."
letter_to_remove_from = 's'
new_string = remove_from_letter_to_dot(original_string, letter_to_remove_from)
# print(new_string)  # Output: "Thi. in this sentence."


# practice  

from bakar_module import   check_password

# check_email_secure()
# check_password()
from test import check_email_secure
from test import check_password
# print(check_email_secure())
password = input("Enter your Password: ")
if check_password(password):
    print("password is store in database")
else:
    pass