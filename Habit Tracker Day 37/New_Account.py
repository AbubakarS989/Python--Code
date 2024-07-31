
import requests
from Graph_Setup import Graphs_Setup
from colorama import Fore, Back, Style, init #For Colors
init()



#? List of functions Created in this file:
# 1:  sign_up() 
# 2:  Graphs()
# 3:  update_user()
# 4:  delete_user()
# 5: word_check()
class Account_Settings_HBT_CWA:

    def __init__(self):
        self.pixela_endpoint = "https://pixe.la/v1/users"
        self.header = ""

    def sign_up(self):
        """
        For New Account:
        Input not as parameter, it ask after run the function
        Input 1: New Username
        Input 1: New Token - make it complex
        """
            
        print(f"--------------------      {Fore.GREEN}Habit Tracker{Style.RESET_ALL}          -------------------\n")
        print(f"----------------    {Fore.LIGHTMAGENTA_EX}Welcome to  Sign Up Screen{Style.RESET_ALL}     -----------------\n")
        print(f"---------------         {Fore.LIGHTYELLOW_EX}Code With Abubakar{Style.RESET_ALL}             -------------\n")


        self.User_Name = input("Enter your New  Username: ")
        self.Token = input("Enter your New Token: ")


        # Program Exit, in case none of them is entered
        if not self.User_Name or not self.Token:
            print("Please Enter your details.")
            exit()


        print(f"""{Fore.RED}Important Note{Style.RESET_ALL}: 
                Store Your {Fore.YELLOW}[Username]{Style.RESET_ALL} and {Fore.YELLOW}[Token]{Style.RESET_ALL} at safe Place.
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


        # Send Request to APi for create an Account
        try:
            r = requests.post(url=self.pixela_endpoint, json=new_params)
            # print(r.text)
            data = r.json()
            if not data["message"] == "This user already exist.":
                print("--------------  Your Account is Created Successfully. -----------------\n")
                print("------------       Code With Abubakar                -----------------\n")
                print(f"Visit The following [{Fore.RED}URL{Style.RESET_ALL}] to View your profile:\n")
         
                #? Output of json is:
                    # {"message":"Success. Let's visit https://pixe.la/@yourusername , it is your profile page!","isSuccess":true}
                # I Extract Particular sentence, When new Account is created Successfully
                txt=data["message"]
                
                # ? To Extract this specific sentence [Let's visit https://pixe.la/@yourusername , it is your profile page!]   
                sentence=txt.split(". ")
                # print(sentence[1])  
                print(f"\t\t :> {Fore.GREEN}{sentence[1]}{Style.RESET_ALL}")
            else:
                print(f"{data["message"]}\n")

        except requests.exceptions.HTTPError as e:
            print(f"{Fore.RED}Failed to Create an account:{Style.RESET_ALL}{e} ")
            


    #? After Signup, Graph section is display to Each New User
    def Graphs(self):
        """
        Execute the Graph Setup File
        """
        screen = Graphs_Setup()
        screen.New_Graph(self.User_Name, self.Token)



    def update_user(self):
        """
        Update User Token
        Input not as parameter, it ask after run the function
        Input 1: Username
        Input 2: Old Token
        Input 3: New Token
        """
        
        print(f"--------------      {Fore.GREEN}Habit Tracker{Style.RESET_ALL}               -------------\n")
        print(f"--------------  {Fore.LIGHTMAGENTA_EX}Account Token Update Section{Style.RESET_ALL}    -------------\n")
        print(f"--------------    {Fore.LIGHTYELLOW_EX}Code With Abubakar{Style.RESET_ALL}            -------------\n")
        self.User_Name = input("Enter your  Username: ")
        self.Token = input("Enter your Token: ")
        self.new_token = input("Enter your New Token: ")

        
        # Program Exit, in case none of them is entered
        if not self.User_Name or not self.Token or not self.new_token:
            print("Please Enter your details.")
            exit()


        print(f"""{Fore.RED}Important Note{Style.RESET_ALL}: 
                Store Your New  {Fore.YELLOW}[Token]{Style.RESET_ALL} at secure Place.
                It will always be asked whenever you add your track. 
                like add value, delete, update....
                """)
        
        
        # Update Token endpoint
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
                print(f"--------------  {Fore.LIGHTGREEN_EX}Your Account is Token is Updated {plain_text}fully.{Style.RESET_ALL} -----------------\n")
                print(f"-------------------        {Fore.LIGHTYELLOW_EX}Code With Abubakar{Style.RESET_ALL}         --------------------------\n")
            else:
                print(f"{Fore.LIGHTRED_EX}Failed to update account Token.{Style.RESET_ALL}")
        except requests.exceptions.HTTPError as e:
            print(f"{Fore.RED}Error Found:{Style.RESET_ALL}", e)
            
            
            
    def delete_user(self):
        """
        Delete User Permanently.
        Input not as parameter, it ask after run the function yp
        Input 1: Username
        Input 2: Token
        Input 3: Before delete it ask [yes/no] 
        """
        
        
        print(f"--------------      {Fore.GREEN} Habit Tracker{Style.RESET_ALL}           ----------------\n")
        print(f"--------------  {Fore.LIGHTMAGENTA_EX} Account Deletion Section {Style.RESET_ALL}   ----------------\n")
        print(f"--------------    {Fore.LIGHTYELLOW_EX}Code With Abubakar{Style.RESET_ALL}         ----------------\n")
        
        
        User_Name = input("Enter your Account Username:")
        User_token = input("Enter your Account Token:")
        
        
        delete_endpoint = f"{self.pixela_endpoint}/{User_Name}"
        
        
        ask = input(f"{Fore.LIGHTRED_EX}Are you Sure to delete your Account?{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}[yes/no{Style.RESET_ALL} ").lower()
        if ask == "yes":
            try:
                header = {
                    "X-USER-TOKEN": User_token
                }
                
                
                r = requests.delete(url=delete_endpoint, headers=header)
                data = r.text

                #Send output of [data] to Word Check that slice the sentence and give me [success] word
                plain_text = self.word_check(data)


                if plain_text == "Success":
                    print(f"--------------  {Fore.GREEN}Your Account is Deleted {plain_text}fully.{Style.RESET_ALL} -----------------\n")
                    print(f"------------      {Fore.LIGHTYELLOW_EX}Code With Abubakar{Style.RESET_ALL}                -----------------\n")
                else:
                    print(f"{Fore.RED}Failed to Delete an account{Style.RESET_ALL}")
            except requests.exceptions.HTTPError as e:
                print(f"{Fore.RED}Failed to Delete an account:{Style.RESET_ALL}{e} ")
        elif ask == "no":
            print(f"{Fore.GREEN}The request has been canceled.{Style.RESET_ALL}")



    def word_check(self, data):
        """
        It Slice the sentence and store into list
        Then return [Success] word 
        Basically used for confirmation from Api request
        """
        
        self.data = data
        # To check the response of request
        # Response Example:
        # {"message":"Success. Let's visit https://pixe.la/@yourusername , it is your profile page!","isSuccess":true}
        # so get the keyword [Success] from the text, I create this function to use multiple times
        lst = []
        for i in range(12, 19):
            lst.append(data[i])
        # now join the list items to convert  into plain text
        plain_text = "".join(lst)
        return plain_text


# screen = Account_Settings_HBT_CWA()
# screen.sign_up()
# # screen.update_user()
