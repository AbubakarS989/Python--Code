


from datetime import datetime
import requests
import json , os
from New_Account import Account_Settings_HBT_CWA
from Graph_Setup import Graphs_Setup
from colorama import init, Fore,Style
init()

#? List of functions Created in this file:
# 1:  log_sign() 
# 2:  Home_Screen()
# 3:  Account_Management()
# 4:  if_user_not_found()
# 6:  Graph_Management()
# 5:  add_track()
# 7:  update_track()
# 8:  delete_track()
# 9:  track__particular_value()
# 10: get_entire_value()
# 11: graph_statistics()
# 12: word_check()



class HABIT_TRACKER_CWA:
    
    
    
    def __init__(self):
        # ? Define General Variable used throughout the program.
        self.USER_NAME = ""
        self.TOKEN = ""
        self.graph_id = ""
        self.date = ""
        self.pixela_endpoint = "https://pixe.la/v1/users"
        self.header = {}
        self.current_date = datetime.now().strftime("%Y%m%d")
    
    
        
    def log_sign(self):
        """
        First screen When user run program
        Show options -> login -signup - Exit 
        """
        
        
        print(f"-------------   {Fore.GREEN}Welcome to Habit Tracker{Style.RESET_ALL}   -------------------\n")
        print(f"-----------     {Fore.LIGHTMAGENTA_EX}Sign Up and Log in Screen{Style.RESET_ALL}     ----------------\n")
        print(f"---------         {Fore.LIGHTYELLOW_EX}Code With Abubakar{Style.RESET_ALL}            --------------\n")
        print("\t\t1: Log in")
        print("\t\t2: Sign Up\n")
        
        
        ask=int(input("Enter your Choice: "))
        if ask==1:
            self.Home_Screen()
        elif ask==2:
            sign_up= Account_Settings_HBT_CWA() 
            sign_up.sign_up()
        else:
            print("Invalid choice. Please try again.")
            exit()
        
        
        
    def Home_Screen(self):
        '''
        Input not as parameter, it ask after run the function
        Login Screen
        Input 1: User Name
        Input 2: Token
        Display Options to the user after authentication.
            1: Add your today Track.
            2: Update your particular Track.
            3: Delete your particular Track.
            4: Get your particular Track Value
            5: Get your Entire Track
            6: Get your Graph Statistics
            7: Account Management
            8: Graph Management
            9: Exit
        In case of invalid user, display login-signup screen
        '''
        
        
        # ? Get Login Details, then display further options.
        print(f"----------------            {Fore.GREEN}Habit Tracker{Style.RESET_ALL}        -------------------\n")
        print(f"-------------          {Fore.LIGHTMAGENTA_EX}Welcome to Log In Screen{Style.RESET_ALL}    -----------------\n")
        print(f"-----------              {Fore.LIGHTYELLOW_EX}Code With Abubakar{Style.RESET_ALL}          ---------------\n")
        self.USER_NAME = input("Enter your Username: \n")
        self.TOKEN = input("Enter your Token: \n")
        
    
        self.header = {
            "X-USER-TOKEN": self.TOKEN
        }
        
        
        # Encounter the error, if user enter none of them
        if not self.USER_NAME or not self.TOKEN :
            print("Please Enter your details.")
            exit()
        
            
        #! User Authentication: Check user exist or not 
        try:
            r=requests.get(url=f"https://pixe.la/@{self.USER_NAME}")
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            self.if_user_not_found()
                
                
        if r:    
            print(f"------------------      {Fore.LIGHTGREEN_EX}User Verified{Style.RESET_ALL}    -------------------\n")
            print(f"-----------       Select one of following{Style.RESET_ALL}     -------------\n")


            print(f"""{Fore.LIGHTYELLOW_EX}
                1: Add your today Track.
                2: Update your particular Track.
                3: Delete your particular Track.
                4: Get your particular Track Value
                5: Get your Entire Track
                6: Get your Graph Statistics
                7: Account Management
                8: Graph Management
                9: Exit
                {Style.RESET_ALL}""")
            choice = int(input("Enter your choice: "))
            
            
            if choice == 1:
                    self.add_track()
            elif choice == 2:
                self.update_track()
                pass
            elif choice == 3:
                self.delete_track()
                pass
            elif choice == 4:
                self.track__particular_value()
            elif choice == 5:
                self.get_entire_value()
            elif choice == 6:
                    self.graph_statistics()
            elif choice == 7:
                self.Account_Management()
            elif choice == 8:
                self.Graph_Management()
            elif choice == 9:
                print("Closing the program.....")
                exit()
            else:
                print("Invalid choice. Please try again.")
                exit()
            
            
                
    def Account_Management(self):
        """
        Display Options:
        1: Update Account Credentials
        2: Delete Account permanently
        3: Exit
        """


        print(f"-------------------     {Fore.GREEN}Habit Tracker{Style.RESET_ALL}             ---------------\n")
        print(f"----------------  {Fore.LIGHTMAGENTA_EX}Welcome to Account Management{Style.RESET_ALL}      ------------\n")      
        print(f"-------------          {Fore.LIGHTYELLOW_EX}Code With Abubakar{Style.RESET_ALL}             -----------\n")
        print(f"-----------        {Fore.LIGHTBLUE_EX}Select one of following{Style.RESET_ALL}              ----------\n")
        print(f"""{Fore.LIGHTYELLOW_EX}
                1: Update your Account Token
                2: Delete Your Account Permanently
                3: Exit
                {Style.RESET_ALL}""")
        choice = int(input("Enter your choice: "))
        
        
        if choice ==1:
            update_user=Account_Settings_HBT_CWA()
            update_user.update_user()
        elif choice==2:
            del_user=Account_Settings_HBT_CWA()
            del_user.delete_user()
        elif choice==3:
            print("Closing the program.....")
            exit()
        else:
            print("Invalid choice. Please try again.")
            exit()
            
            
            
            
    def if_user_not_found(self):
        """
        Display Options:
        1: Create New Account
        2: Back to login screen
        3: Exit
        """
    
    
        print(f"---------------------      {Fore.RED}User not found{Style.RESET_ALL}    ----------------------\n")
        print(f"--------------------       {Fore.GREEN}Habit Tracker{Style.RESET_ALL}         -------------------\n")
        print(f"----------------      {Fore.LIGHTBLUE_EX}Select one of the following{Style.RESET_ALL}     -------------------")
        print(f"""{Fore.LIGHTYELLOW_EX}1: Create New Account.
2: Back to login Screen.                     
3: Exit{Style.RESET_ALL}""")
        
        
        ask=int(input("Enter your Choice: "))
        try:
            if ask==1:
                sign_up= Account_Settings_HBT_CWA() 
                sign_up.sign_up()
            elif ask==2:
                self.Home_Screen()
            elif ask==3:
                print("Closing the program.....")
                exit()
        except ValueError:
            print(" Invalid Input, Try Again ")
        
        
        
    def Graph_Management(self):
        """
        Display Options for graph Customization
        1: Create New Graph
        2: Update Graph Credentials
        3: View Your Graph 
        4: Delete Your Graph Permanently
        5: Exit
        """
        
        
        print(f"-------------            {Fore.GREEN}Habit Tracker{Style.RESET_ALL}               -------------------\n")
        print(f"-------------   {Fore.LIGHTMAGENTA_EX}Welcome to Graph Settings Screen{Style.RESET_ALL}     -------------------\n")      
        print(f"------------         {Fore.LIGHTYELLOW_EX}Code With Abubakar{Style.RESET_ALL}             -------------------\n")
        print(f"-------------    {Fore.LIGHTBLUE_EX}Select one of following{Style.RESET_ALL}             -------------------\n")
        print(f"""{Fore.YELLOW}
                1: Create New Graph
                2: Update Graph Credentials
                3: View Your Graph 
                4: Delete Your Graph Permanently
                5: Exit
                {Style.RESET_ALL}""")
        
        
        # Initialize the Graph Modules
        graph_settings=Graphs_Setup()
        
        
        choice = int(input("Enter your choice: "))
        if choice ==1:
            graph_settings.New_Graph(self.TOKEN, self.USER_NAME)
        elif choice==2:
            graph_settings.update_graph(self.USER_NAME, self.TOKEN)
        elif choice==3:
            graph_settings.view_graph(self.USER_NAME)
        elif choice==4:
            graph_settings.delete_graph(self.USER_NAME, self.TOKEN)
        elif choice==5:
            print("Closing the program.....")
            exit()
        else:
            print("Invalid choice. Please try again.")
            exit()
            
            
            
    def add_track(self):
        '''
        Input not as parameter, it ask after run the function
        Input 1: Graph ID
        Input 2: Track Record Value
        Input Type :  Set by the user at the of graph creation [int or float ]
        Take value set by the user [hours, miles, kilogram..]
        '''
        
        
        print(f"----------------- {Fore.GREEN}Add your Track{Style.RESET_ALL} ------------------")
        print(f"------------     {Fore.LIGHTYELLOW_EX}Code With Abubakar{Style.RESET_ALL}   -----------------")
        
        
        self.graph_id = input("Enter your Graph ID : ")
        quantity = input("How many hours did you work today? ")
        
        
        data_param = {
            "date": self.current_date,
            "quantity": quantity
        }
        
        
        data_endpoint = f"{self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}"
        # print(data_endpoint)
        try:
            r = requests.post(url=data_endpoint,json=data_param, headers=self.header)
            # r.raise_for_status()
            print(f"{Fore.LIGHTGREEN_EX}Today Record is added successfully!{Style.RESET_ALL}")    
        except requests.exceptions. RequestException as e:
            print(f"{Fore.CYAN}Failed to add track:{Style.RESET_ALL}", e)



    def update_track(self):
        """
        Input not as parameter, it ask after run the function
        Update your Track Value.
        Option 1 -> Today Track; 
                    input 1: Your Track value [float or int]
                    input 2: Graph ID
        Option 2 -> Desire Track;
                    input 1: Day [int]
                    input 2: Month [int
                    input 3: Year [int]
                    input 4: Your Track value [float or int]
                    input 5: Graph ID
        """
        
        
        print(f"----------------- {Fore.GREEN}Update your Track{Style.RESET_ALL} ------------------")
        print(f"------------     {Fore.LIGHTYELLOW_EX}Code With Abubakar{Style.RESET_ALL}   -----------------")
        print(f"-------------    {Fore.LIGHTBLUE_EX}Select one of following{Style.RESET_ALL}   -------------\n")
        print(f"""{Fore.YELLOW}1:Update Current Day Track Record 
2: Update Custom Track Record
3: Exit{Style.RESET_ALL}""")
        
        
        ask=input("Enter your Choice: ")
        try:
            ask=int(ask)
            if ask==1:
                manual_date = datetime.now().strftime("%Y%m%d")
                quantity = input("Enter your update value :")
                self.graph_id = input("Enter your Graph id : ") 
            elif ask==2:
                days = int(input("Enter your desire day to update value [1-31]:"))
                months = int(input("Enter month of that date [1-12] :"))
                year = input("Enter year of that  value [ 2024..]:")
                quantity = input("Enter your update value :")
                self.graph_id = input("Enter your Graph id : ")
                manual_date = datetime(year=year, month=months,day=days).strftime("%Y%m%d")
        except ValueError as e:
            print(f"{Fore.Red}Invalid Input{Style.RESET_ALL}")
            
            
        # ? Setup json format for updating values
        update_value = {
            "quantity": quantity
        }


        # ?  New endpoint for updating existing values
        update_endpoint = f"{self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/{manual_date}"
        try:
            r = requests.put(url=update_endpoint,json=update_value, headers=self.header)
            print(f"{Fore.LIGHTGREEN_EX}Your data is updated successfully.{Style.RESET_ALL}")
        except requests.exceptions.RequestException as e:
            print(f"{Fore.LIGHTCYAN_EX}Failed to update value for{Style.RESET_ALL} {self.date}:", e)



    def delete_track(self):
        """
        Delete Particular Track Permanently
        Input not as parameter, it ask after run the function
        
        Input 1: Day [int]
        Input 2: month [int]
        Input 3: Graph ID
        """
        
        
        print(f"----------------  {Fore.LIGHTRED_EX}Delete your Track{Style.RESET_ALL}  --------------")
        print(f"-------------     {Fore.LIGHTYELLOW_EX}Code With Abubakar{Style.RESET_ALL}   ------------\n")
        
        
        days = int(input("Enter your day  [1-31]:"))
        months = int(input("Enter month of that date [1-12]:"))
        self.graph_id = input("Enter your Graph Id : ")


        # Get manual date
        manual_date = datetime(year=2024, month=months,day=days).strftime("%Y%m%d")


        # ?Endpoint for deleting the value
        del_endpoint = f"{self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/{manual_date}"


        # ? Endpoint for getting the required value
        ''' I used this because, the user can verify the data that he is going to delete before the program permanently deleted it '''
        display_endpoint = f"{self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/{manual_date}"
        
        
        try:
            r = requests.get(url=display_endpoint, headers=self.header)
            r.raise_for_status()
            qty = r.json()
            # print(qty)
            
            get_date = datetime.strptime(manual_date, "%Y%m%d").strftime("%d-%m-%Y")
            
            # get the user value to display for user authentication
            print(f"{Fore.LIGHTRED_EX}Are you sure to delete your following track?{Style.RESET_ALL}: ")
            print(f''' {Fore.LIGHTGREEN_EX}Track Record{Style.RESET_ALL}:
            Date: {get_date}
            Quantity: {qty["quantity"]}''')
            # If user say [yes] the value will deleted permanently
            ask = input("Enter your choice [yes/no]: ").lower()
            if ask == "yes":
                try:
                    r = requests.delete(url=del_endpoint, headers=self.header)
                    print(f"{Fore.LIGHTRED_EX}The value has been deleted successfully.{Style.RESET_ALL}")
                except requests.exceptions.RequestException as e:
                    print(f"{Fore.LIGHTBLUE_EX}Failed to delete value for{Style.RESET_ALL} {manual_date}:", e)
            elif ask == "no":
                print(f"{Fore.LIGHTGREEN_EX}The request has been canceled.{Style.RESET_ALL}")
        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}Failed to get value for {Style.RESET_ALL} {manual_date}:", e)



    def track__particular_value(self):
        '''
        Input not as parameter, it ask after run the function
        Easily get Particular Track Value 
        inputs ->   Day [int]
                    Month [int]
                    Graph ID
        Outputs ->  Date
                    Day
                    Track Value
        '''

        
        # Screen
        print(f"----------------------   {Fore.LIGHTGREEN_EX}Your Particular Track Record{Style.RESET_ALL}     --------------------")
        print(f"------------------          {Fore.LIGHTYELLOW_EX}Code With Abubakar{Style.RESET_ALL}               ----------------\n")
        

        #? Inputs
        days = int(input("Enter your day  [1-31]:"))
        months = int(input("Enter month of that date [1-12]:"))
        self.graph_id = input("Enter your Graph id : ")

        
        # Get manual date
        manual_date = datetime(year=2024, month=months,day=days).strftime("%Y%m%d")

        
        # Get day
        manual_day = datetime.strptime(manual_date,"%Y%m%d").strftime("%A")

        
        # Format the date in decent way for display
        get_date = datetime.strptime(manual_date, "%Y%m%d").strftime("%d-%m-%Y")


        # ? Endpoint to get value from the graph
        get_endpoint = f"{self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/{manual_date}"
        try:
            r = requests.get(url=get_endpoint, headers=self.header)
            r.raise_for_status()
            # print(r.json())
            # print(qty["quantity"])
            qty = r.json()
            print(f"\n{Fore.LIGHTMAGENTA_EX}Track Record{Style.RESET_ALL}:\n")
            print(f"\tDay: {manual_day}\n\tDate: {get_date}\n\tTime: {qty["quantity"]} Hours\n")
        except requests.exceptions.RequestException as e:
            print(f"{Fore.LIGHTRED_EX}Failed to retrieve value for{Style.RESET_ALL} {manual_date}:", e)



    def get_entire_value(self):
        '''
        Input not as parameter, it ask after run the function
        [Input]: Graph ID
        Fetch History of Entire Track Record and store into json
        It display the list -> Day - Date - Track Value
        '''
        
        
        # Define list to get the particular format that can easily store in json file
        dic = {}
        dic1 = {}
        dic2 = {}


        # ? Fetching existing data from the JSON file if it exists
        if os.path.exists("Entire Date.json"):
            try:
                with open("Entire Date.json", "r") as f:
                    dic2 = json.load(f)
            except json.JSONDecodeError:
                dic2 = {}
                
                
        '''
        We can get the particular track from one date to other.
        pixels_paras={
             "from":max_date,
             "to":self.current_date,
             "withBody":True
         }
         '''
         
         
        self.graph_id = input("Enter your Graph id : ")
        
        
        # ? Get the dictionary of dates from the Apis and store each respective date corresponding value
        get_pixels = f"{self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/pixels"
        try:
            r = requests.get(url=get_pixels, headers=self.header)
            r.raise_for_status()
            qty = r.json()

            # Store  all dates into list , that we can get the data of respective date.
            list_of_dates = qty["pixels"]

            for i in list_of_dates:
                # ? Input each date one by one to get the corresponding user track quantity
                # print(i)
                
                manual_date = int(i)
                
                # Endpoint for extracting user track values of desire date
                get_endpoint = f"{self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/{manual_date}"
                try:
                    r = requests.get(url=get_endpoint, headers=self.header)
                    r.raise_for_status()
                    format_change = datetime.strptime(i, "%Y%m%d").strftime("%d-%m-%Y")
                    qty = r.json()
                    # print(qty)

                    # ? Store value of user track  of corresponding date into a dictionary
                    dic[format_change] = qty["quantity"]
                except requests.exceptions.RequestException as e:
                    print(f"Failed to retrieve value from {i} to {self.current_date}:", e)
        except requests.exceptions.RequestException as e:
            print(f"Failed to retrieve value :", e)


        # ? Convert the dictionary into the desired format
        dic1 = [[date, quantity] for date, quantity in dic.items()]
        # print(dic1)
        # check in to protect from error
        
        
        if len(dic) != 0:
            # Screen
            print(f"----------------------     {Fore.LIGHTRED_EX}Your Entire Track {Style.RESET_ALL}    -----------------\n",)
            print(f"--------------------          {Fore.LIGHTYELLOW_EX}Code With Abubakar{Style.RESET_ALL}          -----------------\n")
            
            
            for date, quantity in dic.items():
                Day=datetime.strptime(date,"%d-%m-%Y").strftime("%A")
                print(f"Day: {Day}",f"                  Date: {date}    ",f"                    Time:{quantity} Hour   ")
            
                
            # ? Update data to json file with key date
            dic2["Your Track Record"] = dic1

            # ? Dump the updated data into json file
            with open("Entire Date.json", "w") as f:
                json.dump(dic2, f, indent=4)



    def graph_statistics(self):
        '''
        Input not as parameter, it ask after run the function
        [Input]: Graph ID
        Display comprehensive details about your graph.
        1:Total Pixels Count 
        2:Max Quantity
        3:Min Quantity
        4:Total Quantity
        5:Avg Quantity
        6:Todays Quantity
        7:Yesterday Quantity
        8:Max Date
        9:Mix Date
        '''
        

        # Get ID, for getting stats of the specific graph
        self.graph_id = input("Enter your Graph id :")
        

        # Statistics Endpoint
        # /v1/users/<username>/graphs/<graphID>/stats

        
        stats_endpoint = f"{self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/stats"
        stats_r = requests.get(url=stats_endpoint, headers=self.header)
        graph_stats = stats_r.json()

        
        #? Example:
        # ? This is an example of output of graph Statistics
        # totalPixelsCount":4,"maxQuantity":5,"minQuantity":-5,"maxDate":"2017-12-31","minDate":"2018-01-01","totalQuantity":5,"avgQuantity":1.25,"todaysQuantity":3,"yesterdayQuantity":2}

        
        #? Extract the values from the Output and Store each value as separated Variable,for printing them
        total_pixel=graph_stats["totalPixelsCount"]
        max_quantity=graph_stats["maxQuantity"]
        min_quantity=graph_stats["minQuantity"]
        total_quantity=graph_stats["totalQuantity"]
        avg_quantity=graph_stats["avgQuantity"]
        today_qty=graph_stats["todaysQuantity"]
        yesterday_qty=graph_stats["yesterdayQuantity"]

        
        # Maximum Values with respect date and day
        max_date=graph_stats["maxDate"]
        max_date=datetime.strptime(max_date,"%Y-%m-%d").strftime("%d-%m-%Y")
        max_day=datetime.strptime(max_date,"%d-%m-%Y").strftime("%A")

        
        # Minimum Values with respect date and day
        min_date=graph_stats["minDate"]
        min_date=datetime.strptime(min_date,"%Y-%m-%d").strftime("%d-%m-%Y")
        min_day=datetime.strptime(min_date,"%d-%m-%Y").strftime("%A")

        
        # Output All stats in Decent Format         
        print(f"--------------------      {Fore.GREEN}Graph Statistics{Style.RESET_ALL}       -------------------\n")
        print(f"----------------          {Fore.LIGHTYELLOW_EX}Code With Abubakar{Style.RESET_ALL}        -----------------\n")
        print(f"Total Days you posted       : {total_pixel} Days")
        print(f"Maximum Hours you work      : {max_quantity} hours")
        print(f"Minimum Hours you work      : {min_quantity} hours")
        print(f"Total Working Hours         : {total_quantity} hours")
        print(f"Your Average Hours          : {avg_quantity} hours")
        print(f"Today Work hours            : {today_qty} hours")
        print(f"Yesterday Work hours        : {yesterday_qty} hours")
        print(f"Date on which you work less : {min_day} {min_date} ")
        print(f"Date on which you work more : {max_day} {max_date}")
        
        


#? Create instance from the Class
screen = HABIT_TRACKER_CWA()
screen.log_sign()
# screen = Account_Settings_HBT_CWA()
# screen.sign_up()
# screen.delete_user()
# screen.update_user()
# screen.Graphs() 
# If user run python.exe file, it will hold the cmd.
input("Press Enter to close...")
