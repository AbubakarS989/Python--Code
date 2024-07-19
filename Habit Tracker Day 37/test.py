




# def manual_graph():
#     start=int(input("Enter start day [1-31]:"))
#     end=int(input("Enter end day [1-31]:"))
#     mnth=int(input("Enter your month [1-12]:"))
#     flow=abs(start-end)
#     print(flow)

#     for i in range(start,end+1):
#         print(datetime(year=2024,month=mnth,day=i).strftime("%Y%m%d"))   
#         print(f"Hi {i}\n")


from datetime import datetime
import requests , json

class Main:
    def __init__(self):
        self.USER_NAME = ""
        self.TOKEN = ""
        self.graph_id = "bkrgraph1"
        self.date = ""
        self.pixela_endpoint = "https://pixe.la/v1/users"
        self.header = {}
        self.current_date = datetime.now().strftime("%Y%m%d")    
    
    def options(self):
        print("------------- Welcome to Habit Tracker -------------------\n")
        self.USER_NAME = input("Enter your Username: \n")
        self.TOKEN = input("Enter your Token: \n")
        self.header = {
            "X-USER-TOKEN": self.TOKEN
        }
        print("------------- Select one of them -------------------\n")
        print("""
        1: Add your today Track.
        2: Update your particular Track.
        3: Delete your particular Track.
        4: Get your particular Track Value
        5: Get your Entire Track
        6: Get your Graph Stats
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
            self.track_value()
        elif choice == 5:
            self.get_entire_value()
        elif choice == 6:
            self.graph_status()
        else:
            print("Invalid choice. Please try again.")

    def add_track(self):
        print(self.current_date)
        quantity = input("How many hours did you work today? ")
        data_param = {
            "date": self.current_date,
            "quantity": quantity
        }
        data_endpoint = f"{self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}"
        # data_endpoint=f"{pixela_endpoint}/{USER_NAME}/graphs/{graph_id}"
        try:
            r = requests.post(url=data_endpoint, json=data_param, headers=self.header)
            print("Today Record is added successfully!")
            print(r.text)
        except requests.exceptions.RequestException as e:
            print("Failed to add track:", e)
            
    def update_track(self):
        print("------------ Update your Track ----------")
        days=int(input("Enter your day to update value [1-31]:"))
        months=int(input("Enter month of that date [1-12]:"))
        quantity=input("Enter your update value [hours]:")
        update_value={
            "quantity": quantity  
        }
        #Get manual date
        manual_date=datetime(year=2024,month=months,day=days).strftime("%Y%m%d")
        
        # new endpoint for updating existing values
        update_endpoint=f"{self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/{manual_date}"
        try:
            r=requests.put(url=update_endpoint,json=update_value,headers=self.header)
            print(r.text)
        except requests.exceptions.RequestException as e:
            print(f"Failed to update value for {self.date}:", e)
    def delete_track(self):
        print("------------ Delete your Track ----------")
        days=int(input("Enter your day  [1-31]:"))
        months=int(input("Enter month of that date [1-12]:"))
        #Get manual date
        manual_date=datetime(year=2024,month=months,day=days).strftime("%Y%m%d")
        
        del_endpoint=f"{self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/{manual_date}"
        display_endpoint=f"{self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/{manual_date}"
        # get the user value to display for user authentication 
        r = requests.get(url=display_endpoint, headers=self.header)
        qty=r.json()
        get_date=datetime.strptime(manual_date,"%Y%m%d").strftime("%d-%m-%Y")
        print("Are you sure to delete your following track?: ")
        print(f''' Track Record:  
        Date: {get_date}      
        Quantity: {qty["quantity"]}''') 
        ask=input("Enter your choice [yes/no]: ").lower()
        if ask=="yes":
            try:
                r=requests.delete(url=del_endpoint,headers=header)
                print(r.text)
            except requests.exceptions.RequestException as e:
                print(f"Failed to delete value for {manual_date}:", e)
        elif ask=="no":
            print("The request has been canceled.")

    def track_value(self):
        
        print("------------ Show your Track ----------")
        days=int(input("Enter your day  [1-31]:"))
        months=int(input("Enter month of that date [1-12]:"))
        #Get manual date
        manual_date=datetime(year=2024,month=months,day=days).strftime("%Y%m%d")
        get_date=datetime.strptime(manual_date,"%Y%m%d").strftime("%d-%m-%Y")
        get_endpoint=f"{self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/{manual_date}"
        try:
            r=requests.get(url=get_endpoint,headers=self.header)
            r.raise_for_status()
            # print(r.json())
            # print(qty["quantity"])
            qty=r.json()
            print("\nTrack Record:\n")
            print(f"Date: {get_date} Time: {qty["quantity"]} Hours\n")
        except requests.exceptions.RequestException as e:
            print(f"Failed to retrieve value for {manual_date}:", e)
        
    def get_entire_value(self):
        #? I code this because i want to get the all values from the [first pixel] to the [current date pixel], to make it general i use stats method to get the [first pixel date] for any account
        dic={}
        dic2={}
        stats_endpoint=f"{self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/stats"
        stats_r=requests.get(url=stats_endpoint,headers=self.header)
        max_date=stats_r.json()
        max_date=max_date["maxDate"]
        # lst=[]
        # print(lst.append(str(max_date).split("-")))
        # print(lst)
        # # stats_month=lst[0][1]
        # stats_day=lst[0][2]
        # change date format to input date
        max_date=datetime.strptime(max_date,"%Y-%m-%d").strftime("%Y%m%d")
        
        pixels_paras={
            "from":max_date,
            "to":self.current_date,
            "withBody":True
        }
        print(self.current_date)
        get_pixels = f"{self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/pixels"
        try:
            r = requests.get(url=get_pixels,params=pixels_paras, headers=self.header)
            r.raise_for_status()
            qty=r.json()
            # print(qty)
            list_of_dates=qty["pixels"]
            for i in list_of_dates:
                # enter each date one by one
                # print(i)
                manual_date=int(i)
                get_endpoint=f"{self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/{manual_date}"
                try:
                    r=requests.get(url=get_endpoint,headers=self.header)
                    r.raise_for_status()
                    format_change=datetime.strptime(i,"%Y%m%d").strftime("%d-%m-%Y")
                    qty=r.json()
                    # print(qty)
                    # upload date to dic for printing together 
                    dic[format_change]=qty["quantity"]
                except requests.exceptions.RequestException as e:            
                    print(f"Failed to retrieve value from {max_date} to {self.current_date}:", e)
                    
        except requests.exceptions.RequestException as e:
            print(f"Failed to retrieve value from {max_date} to {self.current_date}:", e)
                
        if len(dic) !=0:
            print("---------------  Your Entire Track Values -----------------\n",)
            print(dic)
            for date, quantity in dic.items():
                print(f"Date: {date} Time:{quantity} Hour")
            # Now Upload data to json file with key date
            dic2[format_change]=dic
            # print(dic2)
            with open("Entire Date.json","w") as f:
                json.dump(dic2,f,indent=4)
                
                
    def graph_status(self):
        # /v1/users/<username>/graphs/<graphID>/stats
        stats_endpoint=f"{self.pixela_endpoint}/{self.USER_NAME}/graphs/{self.graph_id}/stats"
        stats_r=requests.get(url=stats_endpoint,headers=self.header)
        max_date=stats_r.json()
        #? I code this because i want to get the all values from the [first pixel] to the [current date pixel], to make it general i use stats method to get the [first pixel date] for any account
        max_date=max_date["maxDate"]
        lst=[]
        print(lst.append(str(max_date).split("-")))
        print(lst)
        stats_month=lst[0][1]
        stats_day=lst[0][2]
        
        
        
                            
        
        
        
        
screen = Main()
screen.options()


# dic={
#     "hi":89,
#     "hi2":89
#     }

# print(len(dic))

