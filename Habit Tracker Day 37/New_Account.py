
import requests
from Graph_Setup import Graphs_Setup
from colorama import Fore, Back, Style, init # for colors
init()

class Account_Settings_HBT_CWA:

    def __init__(self):
        self.pixela_endpoint = "https://pixe.la/v1/users"
        self.header = ""

    def sign_up(self):

        # Take Important values for registration a user

        print("--------------  Account Creation  Section --------------\n")
        print("--------------     Sign Up Screen         --------------\n")
        print("--------------    Code With Abubakar      -----------------\n")

        self.User_Name = input("Enter your New  Username: ")
        self.Token = input("Enter your New Token: ")

        # exit from program if user don't enter any value
        if not self.User_Name or not self.Token:
            print("Please Enter your details.")
            exit()

        print("""Important Note: 
                Store Your [Username] and [Token] at safe Place.
                It will always be asked whenever you add your track. 
                like add value, delete, update....
                """)

        # Create Dict to send this value to APi for Account Creation
        new_params = {
            "token": self.Token,
            "username": self.User_Name,
            "notMinor": "yes",
            "agreeTermsOfService": "yes"
        }

        # Send Request to create an Account
        try:
            r = requests.post(url=self.pixela_endpoint, json=new_params)
            # print(r.text)
            data = r.json()
            if not data["message"] == "This user already exist.":
                print(
                    "--------------  Your Account is Created Successfully. -----------------\n")
                print(
                    "------------       Code With Abubakar                -----------------\n")
                print(f"Visit The following [{Fore.RED}URL{Style.RESET_ALL}] to View your profile:\n")
                # print(f"{data["message"]}\n")
                txt=data["message"]
                # output Should be
                
                # {"message":"Success. Let's visit https://pixe.la/@yourusername , it is your profile page!","isSuccess":true}
                # ?TO Extract this specific sentence [Let's visit https://pixe.la/@yourusername , it is your profile page!]   
                # I use split method to extract it
                sentence=txt.split(". ")
                # print(sentence[1])  
                print(f"\t\t :> {Fore.GREEN}{sentence[1]}{Style.RESET_ALL}")
            else:
                print(f"{data["message"]}\n")

        except requests.exceptions.HTTPError as e:
            print(f"Failed to Create an account:{e} ")

    def Graphs(self):
        screen = Graphs_Setup()
        screen.New_Graph(self.User_Name, self.Token)

    def update_user(self):
        print("--------------  Account Token Update Section --------------\n")
        print("--------------    Code With Abubakar       -----------------\n")
        self.User_Name = input("Enter your  Username: ")
        self.Token = input("Enter your Token: ")
        self.new_token = input("Enter your New Token: ")

        # exit from program if user don't enter any value
        if not self.User_Name or not self.Token or not self.new_token:
            print("Please Enter your details.")
            exit()

        print("""Important Note: 
                Store Your New  [Token] at safe Place.
                It will always be asked whenever you add your track. 
                like add value, delete, update....
                """)
        # Update endpoint
        Update_endpoint = f"{self.pixela_endpoint}/{self.User_Name}"
        self.header = {
            "X-USER-TOKEN": self.Token
        }
        Request_Body = {
            "newToken": self.new_token
        }
        try:
            r = requests.put(url=Update_endpoint,json=Request_Body, headers=self.header)
            data = r.text
            plain_text = self.word_check(data)
            if plain_text == "Success":
                print(f"--------------  Your Account is Token is Updated {plain_text}fully. -----------------\n")
                print(
                    "-------------------        Code With Abubakar         --------------------------\n")
            else:
                print("Failed to update account Token")
        except requests.exceptions.HTTPError as e:
            print("Error Found: ", e)

    def delete_user(self):
        print("--------------  Account Deletion Section -----------------\n")
        print("--------------  Code With Abubakar -----------------\n")
        User_Name = input("Enter your Account Username:")
        User_token = input("Enter your Account Token:")
        delete_endpoint = f"{self.pixela_endpoint}/{User_Name}"
        ask = input("Are you Sure to delete your Account? [yes/no]: ").lower()
        if ask == "yes":
            try:
                header = {
                    "X-USER-TOKEN": User_token
                }
                r = requests.delete(url=delete_endpoint, headers=header)
                data = r.text
                # send data to func for get the text
                # print(data)
                plain_text = self.word_check(data)

                if plain_text == "Success":
                    print(
                        f"--------------  Your Account is Deleted {plain_text}fully. -----------------\n")
                    print(
                        "------------      Code With Abubakar                -----------------\n")
                else:
                    print("Failed to Delete an account")

            except requests.exceptions.HTTPError as e:
                print(f"Failed to Delete an account:{e} ")
        elif ask == "no":
            print("The request has been canceled.")

    def word_check(self, data):
        self.data = data
        # To check the response of request
        # Response Example:
        # {"message":"Success. Let's visit https://pixe.la/@yourusername , it is your profile page!","isSuccess":true}
        # so get the keyword [Success] from the text, i create this function to use multiple times
        lst = []
        for i in range(12, 19):
            lst.append(data[i])
        # now join the list items to convert  into plain text
        plain_text = "".join(lst)
        return plain_text


# screen = Account_Settings_HBT_CWA()

# # screen.delete_user()
# # screen.update_user()
