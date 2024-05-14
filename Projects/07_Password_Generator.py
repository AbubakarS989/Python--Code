import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Python Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# Generate and print the random numbers

random_letters = ""
random_symbols = ""
random_number = ""

# print("Random letter:")
for i in range(nr_letters):
    random_letters += random.choice(letters)
    # print(random_letters)

# print("Random symbols:")

for i in range(nr_symbols):
    random_symbols += random.choice(symbols)
    # print(random_symbols)
    
# print("Random numbers:")

for i in range(nr_numbers):
    random_number += random.choice(numbers)
    # print(random_number)


number=f"{random_letters}{random_symbols}{random_number}"
password="".join(random.sample(number,len(number)))
#  now make a random number

print(f"Your password is :{password}")


# from Chat Gpt

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password
# PASS
password_length = int(input("Enter the desired password length: "))
generated_password = generate_password(password_length)

print("Generated Password:", generated_password)
