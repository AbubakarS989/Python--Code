# Statement
# Account Class with 2 attributes - balance & account no.
# Create methods for debit, credit and printing the balance

# Features
# debit - minus amount
# credit -add amount
# Total balance


class Bank_Account:
    def __init__(self):
        self.Acount_data = {}

    def credit(self):
        self.Acc_No = int(input("Enter your Account No."))
        credit_v = int(input("Enter your credit amount:"))
        self.Acount_data[self.Acc_No] = credit_v
        print(f"Rs:{credit_v} is credited")
        
    def debit(self):
        self.Acc_No = int(input("Enter your Account No."))
        if self.Acc_No in self.Acount_data:
            if self.Acount_data[self.Acc_No] == 0:
                print("Please add amount to your account !")
            else:
                debit_v = int(input("Enter your debit value:"))
                if debit_v > self.Acount_data[self.Acc_No]:
                    print("Low Balance!")
                else:
                    self.Acount_data[self.Acc_No] -= debit_v
                    print(f"Rs:{debit_v} is debited")
        else:
            print("Account not found!")

    def Total_Balance(self):
        self.Acc_No = int(input("Enter your Account No."))
        if self.Acc_No in self.Acount_data:
            print(f"Your current balance is :{self.Acount_data[self.Acc_No]}")
        else:
            print("Account not found!")


def Bank_Account_fun():
    Account_1 = Bank_Account()
    while True:
        key = int(input(
            "Select one of the below:\n1:Add Amount \n2:Windrow Amount\n3:Check Balance\n"))
        if key == 1:
            Account_1.credit()
        elif key == 2:
            Account_1.debit()
        elif key == 3:
            Account_1.Total_Balance()
        else:
            print("Invalid Input")
            return False


Bank_Account_fun()
