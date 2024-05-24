import random
import json
from User_dashboard import user_select
from Email_emplate import  Send_Email
from email_msg import Email_Msg
# from MSG_Emails import email_msg 
# ! Features
# take name, gmail, password, 4-pin
# check the strengthens of pass and pin
# check email address
# send 4 digit pin to user email for EMail authentication
# save all data into the dictionary in separate file


class User:
    def __init__(self, name, gmail, password, pin):
        self.name = name
        self.gmail = gmail
        self.password = password
        self.pin = pin

    def is_strong_password(self):
        # Check if password has at least 6 characters, contains both letters and numbers
        return len(self.password) >= 6 and any(char.isdigit() for char in self.password) and any(char.isalpha() for char in self.password)

    def is_valid_pin(self):
        # Check if PIN is a 4-digit integer
        return len(str(self.pin)) == 4 and str(self.pin).isdigit()

    def to_dict(self):
        return {
            "name": self.name,
            "gmail": self.gmail,
            "password": self.password,
            "pin": self.pin
        }

class UserManager():
    def __init__(self, filename):
        self.filename = filename
        self.user_data = self.read_data()
        

    def read_data(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
        return data

    def write_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.user_data, file)

    def create_user(self):
        self.name = input("Enter name: ")
        self.gmail = input("Enter Gmail: ")

        # Validate password strength
        while True:
            self.password = input("Enter password: ")
            if len(self.password) < 6 or not any(char.isdigit() for char in self.password) or not any(char.isalpha() for char in self.password):
                print("Password is weak. It must have at least 6 characters and contain both letters and numbers.")
            else:
                break

        # Validate PIN
        while True:
            self.pin = input("Enter PIN: ")
            if len(self.pin) != 4 or not self.pin.isdigit():
                print("Invalid PIN. PIN must be a 4-digit integer.")
            else:
                break
        self.valid_email()
        user = User(self.name, self.gmail, self.password, int(self.pin))
        self.add_user(user)
        

    def add_user(self, user):
        # Generate a unique ID for the user
        id = random.randint(1, 100)
        while id in self.user_data:
            id = random.randint(1, 100)
        self.user_data[id] = user.to_dict()
        self.write_data()
        print("Generated ID:", id)
        print("This is your ID. Save it, as it will be used to access, edit, and for every transaction you make!")
        print("Updated user data:")
        user_select()
        
    def valid_email(self):
        # check email address        
        def check_email(gmail):
            pin=random.randint(1000, 9999)
            subject="Email Authentication Code"
            msg_subject="creating a  new account"
            message=Email_Msg(pin,self.name,self.gmail,msg_subject)
            # Code Send to user EMail
            is_ok=Send_Email(self.gmail,message,subject)  
            if is_ok:
                print("The 4-Digit Pin is send to your Email:")
                while True:
                    get_pin = int(input("Enter your 4-Digit Pin: "))
                    if get_pin == pin:  
                        print("You are ready to go!..")
                        break
                    else:
                        print("Invalid Pin. Try Again.")
            else:
                print("Invalid Gmail. Try Again.")
                self.gmail=input("Enter Email Again: ")
                check_email(self.gmail)
                     
        check_email(self.gmail)
            
            
# File name for storing data
filename = "Json/data.json"

# Create a UserManager instance
user_manager = UserManager(filename)

# # Create a new user
# user_manager.create_user()


