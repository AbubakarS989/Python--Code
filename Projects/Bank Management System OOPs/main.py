from Add_User import user_manager 
from User_dashboard import user_select
from User_dashboard import UserDashboard

# Import required modules for colors and formatting
from colorama import Fore, Style
# 29,247  characters
# Create an instance of UserDashboard for login
login = UserDashboard()

def Bank_Management_System():
    print(Fore.GREEN + "-----------   Welcome to AH-Bank   ------------------\n" + Style.RESET_ALL)
    print(Fore.BLUE + "-----------     Abubakar Hafeez    ------------------\n" + Style.RESET_ALL)
    print("1: " + Fore.YELLOW + "Login" + Style.RESET_ALL + " - to your Bank Account.")
    print("2: " + Fore.YELLOW + "Sign Up" + Style.RESET_ALL + " - Create New Bank Account.")
    print("3: " + Fore.YELLOW + "Exit" + Style.RESET_ALL + " from Bank.")
    key = int(input("Enter your Choice: "))
    if key == 1:
        print(Fore.GREEN + "-----------      LOGIN - BANK      ------------------\n" + Style.RESET_ALL)
        print(Fore.BLUE + "-----------     Abubakar Hafeez    ------------------\n" + Style.RESET_ALL)
        print("1: " + Fore.YELLOW + "Login" + Style.RESET_ALL)
        keys = int(input("2: " + Fore.YELLOW + "Forget Pin or ID" + Style.RESET_ALL + ", Re-create your Pin or ID: "))
        if keys == 1:
            is_ok = login.authenticate_user()
            if is_ok:
                user_select()
        elif keys == 2:
            print(Fore.GREEN + "-----------      FORGET PIN or ID - BANK      ------------------\n" + Style.RESET_ALL)
            print(Fore.BLUE + "-----------     Abubakar Hafeez    ------------------\n" + Style.RESET_ALL)
            print("1: " + Fore.YELLOW + "Forget Pin" + Style.RESET_ALL)
            keys = int(input("2: " + Fore.YELLOW + "Forget ID" + Style.RESET_ALL + ": "))
            if keys == 1:
                login.forgot_pin()
            elif keys == 2:
                login.forgot_id()
    elif key == 2:
        user_manager.create_user()
    elif key == 3:
        print("Have a Good Day. Allah Hafiz")
    else:
        print("Invalid Number.")

# Run the Bank Management System
Bank_Management_System()
