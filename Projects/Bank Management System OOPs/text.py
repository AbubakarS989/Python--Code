import datetime as dt
import json

class UserDashboard:
    def __init__(self):
        self.user_data = self.read_data("Json/data.json")
        self.data = self.read_data("Json/money.json")
        self.transactions = self.read_data("Json/transactions.json")
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
                self.money = self.data.get(str(self.user_id), {}).get("balance", 0)
                self.user_loan = self.data.get(str(self.user_id), {}).get("loan", 0)
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
            self.money += amount
            self.data[str(self.user_id)]["balance"] = self.money
            self.write_data("Json/money.json", self.data)
            self.record_transaction(str(self.user_id), "Deposit", amount)
            print("Amount Deposited Successfully")

    def withdraw(self):
        if self.authenticate_user():
            amount = int(input("Enter your Amount RS: "))
            if amount <= self.money:
                self.money -= amount
                self.data[str(self.user_id)]["balance"] = self.money
                self.write_data("Json/money.json", self.data)
                self.record_transaction(str(self.user_id), "Withdrawal", amount)
                print("Amount Withdrawn Successfully")                
            else:
                print("Insufficient Balance")

    def show_balance(self):
        if self.authenticate_user():
            user_money = self.data[str(self.user_id)]["balance"]
            
            print(f"Your Current Balance is: {user_money}")
            print(f"Loan you have: {self.data[str(self.user_id)]["loan"]} ")

    def get_loan(self):
        if self.authenticate_user():
            self.loan_amount = int(input("Enter your Loan Amount (1-10000): "))
            if self.loan_amount <= self.bank_loan_limit:
                self.user_loan += self.loan_amount
                self.data[str(self.user_id)]["loan"] += self.loan_amount
                self.write_data("Json/money.json", self.data)
                self.record_transaction(self.user_id, "Loan", self.loan_amount)
                print("Loan Deposited to your Account")
                print(f"Current Balance: {self.money}")
                print(f"Loan Amount: {self.loan_amount}")
                print(f"Net Balance: {self.money}")
            else:
                print("Loan Amount exceeds Bank Loan Limit")

    def send_money(self):
        if self.authenticate_user():
            recipient_id = input("Enter the Recipient's Account ID: ")
            if recipient_id in self.user_data:
                recipient_name = self.user_data[recipient_id]["name"]
                amount = int(input(f"Enter Amount to Send to {recipient_name}: "))
                if amount <= self.money:
                    self.money -= amount
                    recipient_balance = self.data.get(recipient_id, {}).get("balance", 0) + amount
                    self.data[recipient_id] = {
                        "balance": recipient_balance,
                        "pin": self.user_data[recipient_id]["pin"],
                        "Date": self.current_date,
                        "loan": self.data.get(recipient_id, {}).get("loan", 0)
                    }
                    self.data[self.user_id]["balance"] = self.money
                    self.write_data("Json/money.json", self.data)
                    self.record_transaction(self.user_id, "Send Money", amount, recipient_id)
                    sender_name = self.user_data[self.user_id]["name"]
                    print(f"Recipient Name: {recipient_name}")
                    print(f"Recipient Account ID: {recipient_id}")
                    print(f"Sender Name: {sender_name}")
                    print(f"Sender Account ID: {self.user_id}")
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
        
    def security_settings(self):
        sett = SecuritySettings(self.user_id, self.user_data[self.user_id]["gmail"], self.user_pin, self.user_data[self.user_id]["password"])
        sett.list_of_settings()

class SecuritySettings(UserDashboard):
    def __init__(self, user_id, gmail, pin, password):
        self.id = user_id
        self.gmail = gmail
        self.pin = pin
        self.password = password

    def list_of_settings(self):
        print("---------SECURITY SETTINGS-----------\n")
        print("1: Delete Account")
        print("2: Change Password")
        print("3: Change PIN")
        print("4: Change Email")
        print("5: Change Number")
        print("6: Whatsapp Authentication ON")
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
                self.change_number()
            elif key == 6:
                self.whatsapp_authentication()
            elif key == 7:
                break
            elif key == 8:
                print("Logging Out...")
                break

    def delete_account(self):
        # Implement account deletion
        pass

    def change_password(self):
        # Implement password change
        pass

    def change_pin(self):
        # Implement PIN change
        pass

    def change_email(self):
        # Implement email change
        pass

    def change_number(self):
        # Implement number change
        pass

    def whatsapp_authentication(self):
        # Implement WhatsApp authentication
        pass

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
            dashboard.security_settings()
        elif key == 7:
            print("Logging Out...")
            break

# Run the user selection
user_select()
