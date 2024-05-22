from Add_User import user_manager 
from User_dashboard import user_select
from User_dashboard import UserDashboard

# ! User Management system  is
#  call  create user  method directly 
# user_select()


# Enter name: Black Rose
# Enter Gmail: na706343@gmail.com
# Enter password: fgr9y&*)(0
# Enter PIN: 9899
# Enter your 4-Digit Pin: 6257
# You are ready to go!..
# Generated ID: 44
# create dashboard
login=UserDashboard()

def Bank_Management_System():
    print("-----------   Welcome to AH-Bank   ------------------\n")
    print("-----------     Abubakar Hafeez    ------------------\n")
    print("1: Login- to your Bank Account.")
    print("2: Sign Up - Create New Bank Account.")
    print("3: Exit from Bank. ")
    key=int(input("Enter your Choice: "))
    if key==1:
        print("-----------      LOGIN - BANK      ------------------\n")
        print("-----------     Abubakar Hafeez    ------------------\n")
        print("1: Login  : ")
        keys=int(input("2: Forget Pin or ID, Re-create your Pin or ID: "))
        if keys==1:
            is_ok=login.authenticate_user()
            if is_ok:
                user_select()
        elif keys==2:
            print("-----------      FORGET PIN or ID - BANK      ------------------\n")
            print("-----------     Abubakar Hafeez    ------------------\n")
            print("1: Forget Pin  : ")
            keys=int(input("2: Forget ID  :"))
            if keys==1:
                login.forgot_pin()
            elif keys==2:
                login.forgot_id()
    elif key==2:
        user_manager.create_user()
    elif key==3:
        print("Have a Good Day. Allah Hafiz")
    else:
        print("Invalid Number.")
    


Bank_Management_System()


def forgot_id(self):
        print("1: Verify by Email")
        print("2: Verify by PIN")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            email = input("Enter your registered Email: ")
            found = False
            for user_id, user_info in self.user_data.items():
                if user_info["gmail"] == email:
                    self.send_verification_code(email)
                    verification_code = input("Enter the verification code sent to your email: ")
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

    
    
