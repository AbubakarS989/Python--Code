


from datetime import datetime
import requests
import json , os
from New_Account import Account_Settings_HBT_CWA
from Graph_Setup import Graphs_Setup

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
        print("------------- Welcome to Habit Tracker -------------------\n")
        print("------------- Sign Up and Log in Screen -------------------\n")
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
        Display Number of option.
        Input 1: User Name
        Input 2: Token
        Verify the user otherwise program exist 
        '''
        # ? Get Login Details, then display further options.
        print("-------------            Habit Tracker           ------------------\n")
        print("------------- Welcome to Log In Screen Habit Tracker -------------------\n")
        self.USER_NAME = input("Enter your Username: \n")
        self.TOKEN = input("Enter your Token: \n")
        self.header = {
            "X-USER-TOKEN": self.TOKEN
        }
        
        #! User Authentication: Check user exist or not 
        # Encounter the error
        if not self.USER_NAME or not self.TOKEN :
            print("Please Enter your details.")
            exit()
            
        try:
            r=requests.get(url=f"https://pixe.la/@{self.USER_NAME}")
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            self.if_user_not_found()
                
                
        if r:
            print("-------------     User Verified    -------------------\n")
                
            print("------------- Select one of following -------------------\n")
            print("""
                1: Add your today Track.
                2: Update your particular Track.
                3: Delete your particular Track.
                4: Get your particular Track Value
                5: Get your Entire Track
                6: Get your Graph Statistics
                7: Account Management
                8: Graph Management
                9: Exit
                """)
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
        print("-------------            Habit Tracker               -------------------\n")
        print("-------------   Welcome to Account Settings Screen   -------------------\n")      
                
        print("-------------    Select one of following             -------------------\n")
        print("""
                1: Update your Account Token
                2: Delete Your Account Permanently
                3: Exit
                """)
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
    
        print("-----------------         User not found         ------------------\n")
        print("-----------------         Habit Tracker           ------------------\n")
        print("-------------     Select one of the following  ------------------")
        print("""1: Create New Account.
2: Back to login Screen.                     
3: Exit""")
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
        print("-------------            Habit Tracker               -------------------\n")
        print("-------------   Welcome to Graph Settings Screen   -------------------\n")      
                
        print("-------------    Select one of following             -------------------\n")
        print("""
                1: Create New Graph
                2: Update Graph Credentials
                3: View Your Graph 
                4: Delete Your Graph Permanently
                5: Exit
                """)
        graph_settings=Graphs_Setup()
        choice = int(input("Enter your choice: "))
        if choice ==1:
            graph_settings.New_Graph(self.TOKEN, self.USER_NAME)
        elif choice==2:
            graph_settings.update_graph()
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
        '''Add new track to graph 
           Take number of hours as an input
           Input Type :  Float
        '''
        
        self.graph_id = input("Enter your Graph id : ")
        quantity = input("How many hours did you work today? ")
        data_param = {
            "date": self.current_date,
            "quantity": quantity
        }
        data_endpoint = f"{self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}"
        # data_endpoint=f"{pixela_endpoint}/{USER_NAME}/graphs/{graph_id}"
        try:
            r = requests.post(url=data_endpoint,json=data_param, headers=self.header)
            print("Today Record is added successfully!")    
        except requests.exceptions.RequestException as e:
            print("Failed to add track:", e)

    def update_track(self):
        """
        Update your desire track.
        input 1: Day [int]
        input 2: Month [int]
        input 3: Your Track value in [float]
        """
        print("------------ Update your Track ----------")
        days = int(input("Enter your desire day to update value [1-31]:"))
        months = int(input("Enter month of that date [1-12]:"))
        quantity = input("Enter your update value [hours]:")
        self.graph_id = input("Enter your Graph id : ")

        # ? Data is updated through this format
        update_value = {
            "quantity": quantity
        }

        # Get manual date
        manual_date = datetime(year=2024, month=months,day=days).strftime("%Y%m%d")

        # ?  New endpoint for updating existing values
        update_endpoint = f"{self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/{manual_date}"
        try:
            r = requests.put(url=update_endpoint,json=update_value, headers=self.header)
            print("Your data is updated successfully")
        except requests.exceptions.RequestException as e:
            print(f"Failed to update value for {self.date}:", e)

    def delete_track(self):
        '''
        Delete Particular Track
        Input 1: Day [int]
        Input 2: month [int]
        It ask [yes/no] before permanently deleting the value
        '''
        print("------------ Delete your Track ----------")
        days = int(input("Enter your day  [1-31]:"))
        months = int(input("Enter month of that date [1-12]:"))
        self.graph_id = input("Enter your Graph id : ")

        # Get manual date
        manual_date = datetime(year=2024, month=months,day=days).strftime("%Y%m%d")

        # ?Endpoint for deleting the value
        del_endpoint = f"{self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/{manual_date}"

        # ? Endpoint for getting the required value
        ''' I used this because, the user verify the data that he want to delete before the program permanently deleted it '''
        display_endpoint = f"{self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/{manual_date}"
        try:
            r = requests.get(url=display_endpoint, headers=self.header)
            r.raise_for_status()
            qty = r.json()
            # print(qty)
            
            get_date = datetime.strptime(manual_date, "%Y%m%d").strftime("%d-%m-%Y")
            
            # get the user value to display for user authentication
            print("Are you sure to delete your following track?: ")
            print(f''' Track Record:
            Date: {get_date}
            Quantity: {qty["quantity"]}''')
            # If user say [yes] the value will deleted permanently
            ask = input("Enter your choice [yes/no]: ").lower()
            if ask == "yes":
                try:
                    r = requests.delete(url=del_endpoint, headers=self.header)
                    print("The value has been deleted successfully.")
                except requests.exceptions.RequestException as e:
                    print(f"Failed to delete value for {manual_date}:", e)
            elif ask == "no":
                print("The request has been canceled.")
        except requests.exceptions.RequestException as e:
            print(f"Failed to get value for {manual_date}:", e)


    def track__particular_value(self):
        '''
        Easily track your day
        input 1: Day [int]
        input 2: Month [int]
        It display the value corresponding to the entered date by user
        '''
        print("------------ Show your Track ----------")
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
            print("\nTrack Record:\n")
            print(f"\tDay: {manual_day}\n\tDate: {get_date}\n\tTime: {qty["quantity"]} Hours\n")
        except requests.exceptions.RequestException as e:
            print(f"Failed to retrieve value for {manual_date}:", e)

    def get_entire_value(self):
        '''
        Get History, store in json file
        It display the list of days you posted the value  
        No inputs
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
        """
        stats_endpoint=f"{self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/stats"
        stats_r=requests.get(url=stats_endpoint,headers=self.header)
        max_date=stats_r.json()
        max_date=max_date["maxDate"]
        lst=[]
        print(lst.append(str(max_date).split("-")))
        print(lst)
        # stats_month=lst[0][1]
        stats_day=lst[0][2]
        """

        # change date format to input date
        """ max_date=datetime.strptime(max_date,"%Y-%m-%d").strftime("%Y%m%d") """

        ''' pixels_paras={
             "from":max_date,
             "to":self.current_date,
             "withBody":True
         }
         '''
        self.graph_id = input("Enter your Graph id : ")
        # ? Get the dictionary of dates
        get_pixels = f"{self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/pixels"
        try:
            r = requests.get(url=get_pixels, headers=self.header)
            r.raise_for_status()
            qty = r.json()

            # Store dates into list
            list_of_dates = qty["pixels"]

            for i in list_of_dates:
                # ? Input each date one by one to get the corresponding value
                # print(i)
                manual_date = int(i)
                # Endpoint for extracting values of desire date
                get_endpoint = f"{self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/{manual_date}"
                try:
                    r = requests.get(url=get_endpoint, headers=self.header)
                    r.raise_for_status()
                    format_change = datetime.strptime(i, "%Y%m%d").strftime("%d-%m-%Y")
                    qty = r.json()
                    # print(qty)

                    # ? Store value of corresponding date into a dictionary
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
            print("---------------  Your Entire Track Values -----------------\n",)
            for date, quantity in dic.items():
                print(f"Date: {date} Time:{quantity} Hour")

            # ? Update data to json file with key date
            dic2["Your Track Record"] = dic1

            # ? Put the updated data into json file
            with open("Entire Date.json", "w") as f:
                json.dump(dic2, f, indent=4)

    def graph_statistics(self):
        '''
        Display comprehensive details about your graph
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
        self.graph_id = input("Enter your Graph id :")
        # /v1/users/<username>/graphs/<graphID>/stats
        stats_endpoint = f"{self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/stats"
        stats_r = requests.get(url=stats_endpoint, headers=self.header)
        graph_stats = stats_r.json()
        #? Example Output from APi
        # totalPixelsCount":4,"maxQuantity":5,"minQuantity":-5,"maxDate":"2017-12-31","minDate":"2018-01-01","totalQuantity":5,"avgQuantity":1.25,"todaysQuantity":3,"yesterdayQuantity":2}
        
        #? store each value as separated VAr to get the desire formate
        total_pixel=graph_stats["totalPixelsCount"]
        max_quantity=graph_stats["maxQuantity"]
        min_quantity=graph_stats["minQuantity"]
        total_quantity=graph_stats["totalQuantity"]
        avg_quantity=graph_stats["avgQuantity"]
        today_qty=graph_stats["todaysQuantity"]
        yesterday_qty=graph_stats["yesterdayQuantity"]
        # MAX 
        max_date=graph_stats["maxDate"]
        max_date=datetime.strptime(max_date,"%Y-%m-%d").strftime("%d-%m-%Y")
        max_day=datetime.strptime(max_date,"%d-%m-%Y").strftime("%A")
        # MIN
        min_date=graph_stats["minDate"]
        min_date=datetime.strptime(min_date,"%Y-%m-%d").strftime("%d-%m-%Y")
        min_day=datetime.strptime(min_date,"%d-%m-%Y").strftime("%A")
        # Output in decent Format 
        print("---------------  Graph Statistics -----------------\n")
        print(f"Total Days you posted  : {total_pixel} Days")
        print(f"Maximum Hours you work : {max_quantity} hours")
        print(f"Minimum Hours you work : {min_quantity} hours")
        print(f"Total Working Hours    : {total_quantity} hours")
        print(f"Your Average Hours     : {avg_quantity} hours")
        print(f"Today Work hours       : {today_qty} hours")
        print(f"Yesterday Work hours   : {yesterday_qty} hours")
        print(f"Date on which you work less:{min_day} {min_date} ")
        print(f"Date on which you work more: {max_day} {max_date}")
        
        


#? Create instance from the Class
screen = HABIT_TRACKER_CWA()
screen.log_sign()
# screen = Account_Settings_HBT_CWA()
# screen.sign_up()
# screen.delete_user()
# screen.update_user()
# screen.Graphs() 
input("Press Enter to close...")
# 1.15 min