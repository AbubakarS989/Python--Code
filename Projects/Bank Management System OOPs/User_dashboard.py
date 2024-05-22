import datetime as dt
import json

# if id in not found to create new account
# after log in with id and (pin or password)
# USer dashboard
# add money
# withdraw money
# show balance
# send money
# loan
# Security settings ->
# delete Account-->
# Account name
# id
# pin
# gmail code for authentication
# change pass
# change pin
# change email
# change numbers wts

#! all these changes need two step verification


class User_Dashboard:
    def __init__(self, user_id, gmail, pin, password):
        self.id = user_id
        self.gmail = gmail
        self.pin = pin
        self.password = password
        self.data = self.read_money()
        self.money = self.data.get(str(self.id), {}).get("balance", 0)
        self.current_date = current_date = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    def read_money(self):
        try:
            with open("Json/money.json", "r") as file:
                money_data = json.load(file)
        except FileNotFoundError:
            money_data = {}
        return money_data

    def write_money(self):
        with open("Json/money.json", "w") as file:
            json.dump(self.data, file)

    def money_dict(self):
        
        return {
            "balance": self.money,
            "gmail": self.gmail,
            "pin": self.pin,
            "Date": self.current_date
        }
    def add_money(self):
        self.user_id = int(input("Enter your Account ID:"))
        if self.id == self.user_id:
            amount  = int(input("Enter your Amount RS:"))
            self.user_pin = int(input("Enter your 4-Digit Pin to Deposit Amount: "))
            if self.pin == self.user_pin:
                print("Amount Deposit")
                self.money+=amount
                self.data[str(self.id)]=self.money_dict()
                self.write_money()
            else:
                print("Invalid PIN,Try Again.")
                self.add_money()
        else:
            print("Invalid ID. User Not Found.")
            return False
        

    def withdraw(self):
        pass

    def showBalance(self):
        pass

    def send_money(self):
        pass

    def get_loan(self):
        pass

    def security_settings(self):
        sett = Security_Settings(self.id, self.gmail, self.pin, self.password)
        sett.list_of__settings()


# Security settings ->
        # delete Account-->
        # Account name
        # id
        # pin
        # gmail code for authentication
        # change pass
        # change pin
        # change email
        # change numbers wts

    def del_account(self):
        pass


class Security_Settings(User_Dashboard):
    def __init__(self, user_id, gmail, pin, password):
        self.id = user_id
        self.gmail = gmail
        self.pin = pin
        self.password = password

    def list_of__settings(self):
        print("---------SECURITY SETTINGS-----------\n")
        print("1: Delete Account\n")
        print("2: Change Password\n")
        print("3: Change PIN\n")
        print("4: Change Email\n")
        print("5: Change Number\n")
        print("6: Whatsapp Authentication ON.\n")
        print("7: Back To USER DASHBOARD.\n")
        print("8: Exit.\n")
        self.key = int(input("Enter your choice: "))

        # pass key
        while True:
            if self.key == 1:
                pass
            elif self.key == 2:
                dashboard.withdraw()
            elif self.key == 3:
                dashboard.showBalance()
            elif self.key == 4:
                dashboard.send_money()
            elif self.key == 5:
                dashboard.get_loan()
            elif self.key == 6:
                dashboard.security_settings()
            elif self.key == 7:
                dashboard.security_settings()
            elif self.key == 8:
                print("Logging Out....")
                break


def user_select(user_id, gmail, pin, password):

    dashboard = User_Dashboard(user_id, gmail, pin, password)
    print("---------USER DASHBOARD-----------\n")
    print("Select One of the following: \n")
    print("1: Add Money \n")
    print("2: Withdraw Money \n")
    print("3: Show Balance \n")
    print("4: Send Money \n")
    print("5: Get Loan \n")
    print("6: Further Security Settings...\n")
    print("7: Exit \n")
    key = int(input("Enter your Choice : "))

    while True:
        if key == 1:
            dashboard.add_money()
        elif key == 2:
            dashboard.withdraw()
        elif key == 3:
            dashboard.showBalance()
        elif key == 4:
            dashboard.send_money()
        elif key == 5:
            dashboard.get_loan()
        elif key == 6:
            dashboard.security_settings()
        elif key == 7:
            print("Logging Out....")
            break
