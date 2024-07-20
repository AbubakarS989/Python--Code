
from datetime import datetime
import requests
import json
import os


class HABIT_TRACKER_CWA:
    def __init__(self):
        # ? Define General Variable used throughout the program.
        self.USER_NAME = ""
        self.TOKEN = ""
        self.graph_id = "bkrgraph1"
        self.date = ""
        self.pixela_endpoint = "https://pixe.la/v1/users"
        self.header = {}
        self.current_date = datetime.now().strftime("%Y%m%d")

    def options(self):
        # ? Get Login Details, then display further options.
        print("------------- Welcome to Habit Tracker -------------------\n")
        self.USER_NAME = input("Enter your Username: \n")
        self.TOKEN = input("Enter your Token: \n")
        self.header = {
            "X-USER-TOKEN": self.TOKEN
        }
        print("------------- Select one of following -------------------\n")
        print("""
        1: Add your today Track.
        2: Update your particular Track.
        3: Delete your particular Track.
        4: Get your particular Track Value
        5: Get your Entire Track
        6: Get your Graph Statistics
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
            self.graph_status()
        else:
            print("Invalid choice. Please try again.")

    def add_track(self):
        '''Add new track to graph 
           Take number of hours as an input
           Input Type :  Float
        '''
        print(self.current_date)
        quantity = input("How many hours did you work today? ")
        data_param = {
            "date": self.current_date,
            "quantity": quantity
        }
        data_endpoint = f"{
            self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}"
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

        update_value = {
            "quantity": quantity
        }

        # Get manual date
        manual_date = datetime(year=2024, month=months,
                               day=days).strftime("%Y%m%d")

        # ?  New endpoint for updating existing values
        update_endpoint = f"{
            self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/{manual_date}"
        try:
            r = requests.put(url=update_endpoint,
                             json=update_value, headers=self.header)
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

        # Get manual date
        manual_date = datetime(year=2024, month=months,
                               day=days).strftime("%Y%m%d")

        # ?Endpoint for deleting the value
        del_endpoint = f"{
            self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/{manual_date}"

        # ? Endpoint: I used this because, the user verify the data that he want to delete before the program permanently deleted it
        display_endpoint = f"{
            self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/{manual_date}"
        r = requests.get(url=display_endpoint, headers=self.header)
        qty = r.json()
        get_date = datetime.strptime(
            manual_date, "%Y%m%d").strftime("%d-%m-%Y")
        # get the user value to display for user authentication
        print("Are you sure to delete your following track?: ")
        print(f''' Track Record:
        Date: {get_date}
        Quantity: {qty["quantity"]}''')

        # If user say [yes] the value will deleted permanently
        ask = input("Enter your choice [yes/no]: ").lower()
        if ask == "yes":
            try:
                r = requests.delete(url=del_endpoint, headers=header)
                print(r.text)
            except requests.exceptions.RequestException as e:
                print(f"Failed to delete value for {manual_date}:", e)
        elif ask == "no":
            print("The request has been canceled.")

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
        # Get manual date
        manual_date = datetime(year=2024, month=months,
                               day=days).strftime("%Y%m%d")

        # Format the date in decent way to display
        get_date = datetime.strptime(
            manual_date, "%Y%m%d").strftime("%d-%m-%Y")

        # ? Endpoint to get value from the graph
        get_endpoint = f"{
            self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/{manual_date}"
        try:
            r = requests.get(url=get_endpoint, headers=self.header)
            r.raise_for_status()
            # print(r.json())
            # print(qty["quantity"])
            qty = r.json()
            print("\nTrack Record:\n")
            print(f"Date: {get_date} Time: {qty["quantity"]} Hours\n")
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
        # ? Get the dictionary of dates
        get_pixels = f"{
            self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/pixels"
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
                get_endpoint = f"{
                    self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/{manual_date}"
                try:
                    r = requests.get(url=get_endpoint, headers=self.header)
                    r.raise_for_status()
                    format_change = datetime.strptime(
                        i, "%Y%m%d").strftime("%d-%m-%Y")
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

            with open("Entire Date.json", "w") as f:
                json.dump(dic2, f, indent=4)

    def graph_status(self):
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
        
        # /v1/users/<username>/graphs/<graphID>/stats
        stats_endpoint = f"{
            self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/stats"
        stats_r = requests.get(url=stats_endpoint, headers=self.header)
        graph_stats = stats_r.json()
        # ? I code this because i want to get the all values from the  [first pixel] to the [current date pixel], to make it general i use stats method to get the [first pixel date] for any account
        # totalPixelsCount":4,"maxQuantity":5,"minQuantity":-5,"maxDate":"2017-12-31","minDate":"2018-01-01","totalQuantity":5,"avgQuantity":1.25,"todaysQuantity":3,"yesterdayQuantity":2}
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
        
        
        
        
        
        # lst = []
        # print(lst.append(str(max_date).split("-")))
        # print(lst)
        # stats_month = lst[0][1]
        # stats_day = lst[0][2]


screen = HABIT_TRACKER_CWA()
screen.options()
