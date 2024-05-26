
# !Functions List that are created in this file
# Class User dashboard
# read_data
# write_data
# authenticate_user
# assigning new id at the time of sign up 
# email verification is used while adding new user as well as in all security options
# money_dict
# add_money
# withdraw
# show_balance
# get_loan
# send_money
# record_transaction
# forgot_pin
# forgot_id
# security_settings
# Class User Security Settings
# Account Delete
# Change password
# Change pin
# Change EMail
# Wts verification on




#! all these changes need two step verification
import datetime as dt
import json
import random
# from Security_Settings_file import SecuritySettings
from Email_emplate import Send_Email
from email_msg import Email_Msg
from email_msg_send_money import Email_Msg_Send_MONey
from Account_del_msg import Email_Msg_Delete_Account


class UserDashboard:
    def __init__(self): 
        self.user_data = self.read_data("Json/data.json")
        self.data = self.read_data("Json/money.json")
        self.transactions = self.read_data("Json/transactions.json")
        self.deleted_users = self.read_data("Json/deleted_users.json")
        self.current_date = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.bank_loan_limit = 10000
        self.user_id = None
        self.user_pin = None
        self.money = 0
        self.user_loan = 0

    def read_data(self, file_path):
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
        return data

    def write_data(self, file_path, data):
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4
                      )

    def authenticate_user(self):
        self.user_id = input("Enter your Account ID: ")
        if str(self.user_id) in self.user_data:
            self.user_pin = int(input("Enter your 4-Digit Pin: "))
            if self.user_data[str(self.user_id)]["pin"] == self.user_pin:
                self.money = self.data.get(
                    str(self.user_id), {}).get("balance", 0)
                self.user_loan = self.data.get(
                    str(self.user_id), {}).get("loan", 0)
                return True
            else:
                print("Invalid PIN, Try Again.")
                return False
        else:
            print("Invalid ID, User Not Found.")
            return False

    def money_dict(self):
        return {
            "balance": self.money,
            "pin": self.user_pin,
            "Date": self.current_date,
            "loan": self.user_loan
        }

    def add_money(self):
        if self.authenticate_user():
            amount = int(input("Enter your Amount RS: "))
             # Check if user's data exists in self.data, if not, initialize it
            if self.user_id not in self.data:
                self.data[self.user_id] = {"balance": 0, "pin": self.user_pin, "Date": self.current_date, "loan": 0}
            self.money += amount
            self.data[self.user_id]["balance"] = self.money
            self.write_data("Json/money.json", self.data)
            self.record_transaction(self.user_id, "Deposit", amount)
            print("Amount Deposited Successfully")

    def withdraw(self):
        if self.authenticate_user():
            amount = int(input("Enter your Amount RS: "))
            if amount <= self.money and amount!=0:
                self.money -= amount
                self.data[self.user_id]["balance"] = self.money
                self.write_data("Json/money.json", self.data)
                self.record_transaction(
                    self.user_id, "Withdrawal", amount)
                print("Amount Withdrawn Successfully")
            else:
                print("Insufficient Balance")

    def show_balance(self):
        if self.authenticate_user():
            user_money = self.data[self.user_id]["balance"]

            print(f"Your Current Balance is: {user_money}")
            print(f"Loan you have: {self.data[self.user_id]["loan"]} ")

    def get_loan(self):
        if self.authenticate_user():
            self.loan_amount = int(input("Enter your Loan Amount (1-10000): "))
            if self.loan_amount <= self.bank_loan_limit:
                self.user_loan += self.loan_amount
                self.data[self.user_id]["loan"] += self.loan_amount
                self.data[self.user_id]["balance"] += self.loan_amount
                self.data[self.user_id]["Date"] = self.current_date
                self.write_data("Json/money.json", self.data)
                self.record_transaction(self.user_id, "Loan", self.loan_amount)
                net_balance = self.money+self.user_loan
                print("Loan Deposited to your Account")
                print(f"Current Balance: {self.money}")
                print(f"Loan Amount: {self.loan_amount}")
                print(f"Net Balance: {net_balance}")
            else:
                print("Loan Amount exceeds Bank Loan Limit")

    def send_money(self):
        if self.authenticate_user():
            recipient_id = input("Enter the Recipient's Account ID: ")
            if recipient_id in self.user_data:
                recipient_name = self.user_data[recipient_id]["name"]
                amount = int(
                    input(f"Enter Amount to Send to {recipient_name}: "))
                if amount <= self.money:
                    self.money -= amount
                    self.recipient_balance = self.data.get(recipient_id, {}).get("balance", 0) + amount
                    self.data[recipient_id] = {
                        "balance": self.recipient_balance,
                        "pin": self.user_data[recipient_id]["pin"],
                        "Date": self.current_date,
                        "loan": self.data.get(recipient_id, {}).get("loan", 0)
                    }
                    self.data[self.user_id]["balance"] = self.money
                    self.write_data("Json/money.json", self.data)
                    self.record_transaction(self.user_id, "Send Money", amount, recipient_id)
                    receiver_gmail=self.user_data[recipient_id]["gmail"]
                    sender_name = self.user_data[self.user_id]["name"]
                    subject="Amount Receive To your Bank Account"
                    print("----------  Send Money   ----------")            
                    print(f"Recipient Name: {recipient_name}")
                    print(f"Recipient Account ID: {recipient_id}")
                    print(f"Sender Name: {sender_name}")
                    print(f"Sender Account ID: {self.user_id}")
                    print(f"Send Amount:{amount}")
                    print(f"Remain Balance:{self.money}")
                    balance=self.recipient_balance
                    msg=Email_Msg_Send_MONey(recipient_name,sender_name,receiver_gmail,amount,balance)
                    Send_Email(receiver_gmail,msg,subject)    
                    print("Amount Sent Successfully")
                else:
                    print("Insufficient Balance")
            else:
                print("Invalid Recipient ID, User Not Found")

    def record_transaction(self, user_id, transaction_type, amount, recipient_id=None):
        transaction = {
            "Date": self.current_date,
            "Transaction Type": transaction_type,
            "Amount": amount,
            "Recipient ID": recipient_id,
            "Recipient Gmail": self.user_data.get(recipient_id, {}).get("gmail", "N/A")
        }
        if user_id in self.transactions:
            self.transactions[user_id].append(transaction)
        else:
            self.transactions[user_id] = [transaction]
        self.write_data("Json/transactions.json", self.transactions)

    def security_settings_module(self):
        if self.authenticate_user():
            security_settings = SecuritySettings(
                self.user_id, self.user_data[self.user_id]["gmail"], self.user_pin, self.user_data[self.user_id]["password"], self.transactions, self.deleted_users)
            security_settings.list_of_settings()

    def forgot_pin(self):
        user_id = input("Enter your Account ID: ")
        self.email = input("Enter your registered Email: ")

        if user_id in self.user_data and self.user_data[user_id]["gmail"] == self.email:
            verification_code = str(random.randint(1000, 9999))
            # Simulate sending the verification code via email
            receiver_name = self.user_data[user_id]["name"]
            msg_subject="want to retrieve your Account PIN"
            message = Email_Msg(verification_code, receiver_name, self.email,msg_subject)
            subject = "Email Authentication Code"
            # Code Send to user EMail
            if Send_Email(self.email, message, subject):

                print(f"A verification code has been sent to your email:")
                entered_code = input(
                    "Enter the verification code sent to your email: ")

                if entered_code == verification_code:
                    new_pin = input("Enter your new 4-digit PIN: ")
                    self.user_data[user_id]["pin"] = int(new_pin)
                    self.write_data("Json/data.json", self.user_data)
                    print("Your PIN has been successfully updated.")
                else:
                    print("Incorrect verification code.")
            else:
                print("Invalid Email.")
        else:
            print("Account ID and email do not match our records.")

    def forgot_id(self):
        print("1: Verify by Email")
        print("2: Verify by PIN")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            email = input("Enter your registered Email: ")
            found = False
            for user_id, user_info in self.user_data.items():
                if user_info["gmail"] == email:
                    self.generated_code = str(random.randint(1000, 9999))
                    receiver_name = self.user_data[user_id]["name"]
                    msg_subject="want to retrieve your Account ID "
                    message = Email_Msg(self.generated_code,receiver_name, email,msg_subject)
                    subject = "Email Authentication Code"
                    Send_Email(email, message, subject)
                    verification_code = input(
                        "Enter the verification code sent to your email: ")
                    if verification_code == self.generated_code:
                        print(f"Your Account ID is: {user_id}")
                        found = True
                        break
            if not found:
                print("Email not found in our records.")

        elif choice == 2:
            pin = int(input("Enter your 4-digit PIN: "))
            found = False
            for user_id, user_info in self.user_data.items():
                if user_info["pin"] == pin:
                    print(f"Your Account ID is: {user_id}")
                    found = True
                    break
            if not found:
                print("PIN not found in our records.")
        else:
            print("Invalid choice.")

# class SecuritySettings(UserDashboard):


class SecuritySettings(UserDashboard):
    def __init__(self, user_id, gmail, pin, password, transactions, deleted_users):
        super().__init__()
        self.transactions = transactions
        self.deleted_users = deleted_users
        self.id = user_id
        self.gmail = gmail
        self.pin = pin
        self.password = password
        self.user_data = self.read_data("Json/data.json")
        self.data = self.read_data("Json/money.json")

    def list_of_settings(self):
        print("---------SECURITY SETTINGS-----------\n")
        print("1: Delete Account")
        print("2: Change Password")
        print("3: Change PIN")
        print("4: Change Email")
        print("5: Change Number")
        print("6: WhatsApp Authentication ON")
        print("7: Back To USER DASHBOARD")
        print("8: Exit")

        while True:
            key = int(input("Enter your choice: "))
            if key == 1:
                self.delete_account()
            elif key == 2:
                self.change_password()
            elif key == 3:
                self.change_pin()
            elif key == 4:
                self.change_email()
            elif key == 5:
                # self.change_number()
                pass
            elif key == 6:
                self.whatsapp_authentication()
            elif key == 7:
                break
            elif key == 8:
                print("Logging Out...")
                exit()

    def delete_account(self):
        confirmation = input(
            "Are you sure you want to delete your account? (yes/no): ")
        if confirmation.lower() == "yes":
            user_id_str = str(self.id)
            if user_id_str in self.user_data:
                verification_code = random.randint(1000, 9999)
                receiver_name = self.user_data[user_id_str]["name"]
                msg_subject="want to delete your account for permanently"
                message = Email_Msg(verification_code,receiver_name, self.gmail,msg_subject)
                subject = "Account Deletion Code"
                # Code Send to user EMail
                if Send_Email(self.gmail, message, subject):
                    print(f"A verification code has been sent to your email:")
                    entered_code = int(
                        input("Enter the verification code sent to your email: "))

                    if entered_code == verification_code:
                        money=self.data[user_id_str]["balance"]
                        subject="Your Account is successfully deleted - Abubakar Bank"
                        msg=Email_Msg_Delete_Account(receiver_name,user_id_str,self.gmail,money)
                        Send_Email(self.gmail,msg,subject)
                        deleted_user_data = {
                            "Date": self.current_date,
                            "user_data": self.user_data[user_id_str],
                            "money_data": self.data.get(user_id_str, {}),
                            "transactions": self.transactions.get(user_id_str, [])
                        }
                        
                        self.deleted_users[user_id_str] = deleted_user_data

                        del self.user_data[user_id_str]
                        if user_id_str in self.transactions:
                            del self.transactions[user_id_str]
                        else:
                            pass
                        if user_id_str in self.data:
                            del self.data[user_id_str]
                        else:
                            pass
                            

                        self.write_data("Json/data.json", self.user_data)
                        self.write_data("Json/money.json", self.data)
                        self.write_data("Json/transactions.json", self.transactions)
                        self.write_data("Json/deleted_users.json", self.deleted_users)
                    
                        print("Account deleted successfully.")
                    else:
                        print("Invalid Code.")
                else:
                    print("Invalid Gmail")
        else:
            print("Account deletion cancelled.")

    def whatsapp_authentication(self):
        print("WhatsApp authentication is now enabled.")
        # Implement WhatsApp authentication logic

    def change_password(self):
        current_password = input("Enter your current password: ")
        verification_code = random.randint(1000, 9999)
        receiver_name = self.user_data[self.id]["name"]
        msg_subject="want to change your Account Password  "
        message = Email_Msg(verification_code, receiver_name, self.gmail,msg_subject)
        subject = "Change Password Authentication Code"
        # Code Send to user EMail
        if Send_Email(self.gmail, message, subject):
            print(f"A verification code has been sent to your email:")
            entered_code = int(
                input("Enter the verification code sent to your email: "))
            if entered_code == verification_code:
                if current_password == self.password:
                    new_password = input("Enter your new password: ")
                    confirm_password = input("Confirm your new password: ")
                    if new_password == confirm_password:
                        self.user_data[self.id]["password"] = new_password
                        self.write_data("Json/data.json", self.user_data)
                        print("Password changed successfully.")
                    else:
                        print("Passwords do not match.")
                else:
                    print("Incorrect current password.")
            else:
                print("Invalid Verification Code")
        else:
            print("Invalid Gmail.")

    def change_pin(self):
        current_pin = int(input("Enter your current 4-digit PIN: "))
        if current_pin == self.pin:
            verification_code = random.randint(1000, 9999)
            receiver_name = self.user_data[self.id]["name"]
            msg_subject="want to change your account PIN"
            message = Email_Msg(verification_code, receiver_name, self.gmail,msg_subject)
            subject = "Change Pin Authentication Code"
            # Code Send to user EMail
            if Send_Email(self.gmail, message, subject):
                print(f"A verification code has been sent to your email:")
                entered_code = int(
                    input("Enter the verification code sent to your email: "))
                if entered_code == verification_code:
                    new_pin = int(input("Enter your new 4-digit PIN: "))
                    confirm_pin = int(input("Confirm your new 4-digit PIN: "))
                    if new_pin == confirm_pin:
                        self.user_data[self.id]["pin"] = new_pin
                        self.write_data("Json/data.json", self.user_data)
                        print("PIN changed successfully.")
                    else:
                        print("PINs do not match.")
                else:
                      print("Invalid Verification Code")
            else:
                print("Invalid Gmail.")
        else:
            print("Incorrect current PIN.")

    def change_email(self):
        current_email = input("Enter your current email: ")
        if current_email == self.gmail:
            verification_code = random.randint(1000, 9999)
            receiver_name = self.user_data[self.id]["name"]
            msg_subject="want to change your Account Gmail"
            message = Email_Msg(verification_code, receiver_name, self.gmail,msg_subject)
            subject = "Change Email Authentication Code"
            # Code Send to user EMail
            if Send_Email(self.gmail, message, subject):
                print(f"A verification code has been sent to your email:")
                entered_code = int(
                    input("Enter the verification code sent to your email: "))
                if entered_code == verification_code:
                    new_email = input("Enter your new email: ")
                    confirm_email = input("Confirm your new email: ")
                    if new_email == confirm_email:
                        self.user_data[self.id]["gmail"] = new_email
                        self.write_data("Json/data.json", self.user_data)
                        print("Email changed successfully.")
                    else:
                        print("Emails do not match.")
                else:
                    print("Invalid Verification Code")
            else:
                print("Invalid Gmail.")
        else:
            print("Incorrect current email.")


def user_select():
    dashboard = UserDashboard()
    while True:
        print("---------USER DASHBOARD-----------\n")
        print("1: Add Money")
        print("2: Withdraw Money") 
        print("3: Show Balance")
        print("4: Send Money")
        print("5: Get Loan")
        print("6: Further Security Settings")
        print("7: Exit")

        key = int(input("Enter your Choice: "))
        if key == 1:
            dashboard.add_money()
        elif key == 2:
            dashboard.withdraw()
        elif key == 3:
            dashboard.show_balance()
        elif key == 4:
            dashboard.send_money()
        elif key == 5:
            dashboard.get_loan()
        elif key == 6:
            dashboard.security_settings_module()
        elif key == 7:
            print("Logging Out...")
            break

# Run the user selection
# user_select()