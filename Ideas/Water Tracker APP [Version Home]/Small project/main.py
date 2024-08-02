from datetime import datetime
import os, json, random
from storing_monthly_data import Monthly_History
from Entire_History_data import Store_History
from Online_WT import Upload_Daily_sheet_WT 

class Testing:
    
    def __init__(self):
        self.current_date = datetime.now().strftime("%d-%m-%Y")
        self.status = ""
        self.can_price = 0
        self.cooler_price = 0
        self.drum_price = 0
        self.bill = 0
        self.paid = 0
        self.dues = 0
        self.M_previous_dues=0
        self.ask=""

 
    
    def Main_Screen(self):
        
        print(f"--------------- Water Tracker [Home Version]  -------------------")
        print(f"---------------         Main Screen           -------------------")
        print(f"---------------    Code With Abubakar         -------------------\n")
        
        
        print(f"""Select one of the following:
1: Enter your Water Tracker
2: Show History of Your Water Track
3: Exit""")
        ask=input(f"Enter your Choice")
        try:
            ask=int(ask)
            if ask==1:
                self.home_screen()
            elif ask==2:
                self.history_option()
            elif ask==3:
                print(f"closing the program......")
                exit()
        except ValueError as e:
            print(f"Invalid Option :{e}")
        
    def history_option(self):
        
        print(f"--------------- Water Tracker [Home Version] --------------------")
        print(f"---------------       History Screen         --------------------")
        print(f"---------------   Code With Abubakar         --------------------\n")
        
        
        print(f"""Select one of the following:
1: Show Monthly History
2: Show Yearly History
3: Exit""")
        ask=input("Enter your Option: ")
        try:
            ask=int(ask)
            if ask==1:
                pass
                history=Monthly_History()
                history.monthly_values()
                
            elif ask==2:
                Entire_History=Store_History()
                Entire_History.yearly_values()
            elif ask==3:
                print(f"closing the program......")
                exit()
        except ValueError as e:
            print(f"Please Enter Valid Option.")      
            
        
        
    def home_screen(self):
        
        
        
        self.ask_h = input("Did you buy [y/n]? ").lower()
        if self.ask_h == "y":
            print("Welcome to tracker testing\n")
            can = int(input("Enter cans: "))
            cooler = int(input("Enter cooler: "))
            drum = int(input("Enter drum: "))
            print(f"your Previous Dues :{self.monthly_dues()}")
            self.calculations(can, cooler, drum)
            self.status = "Present"
        elif self.ask_h == "n":
            
            self.status = "Absent"
            self.calculations(cans=0,cooler=0,drum=0)
            
            
    
    def reading(self):
        try:
            if os.path.exists("Daily_data_WT.json"):
                with open("Daily_data_WT.json", "r") as f:
                    self.data = json.load(f)
            else:
                self.data = {}
            return self.data
        except (IOError, json.JSONDecodeError) as e:
            print(f"Failed to read a file: {e}")       
            return {}
        
    def get_next_id(self):
        if self.data:
            last_id = max(self.data.keys(), key=int)
            return int(last_id) + 1
        return 1  
    
    def storing(self, data):
        with open("Daily_data_WT.json", "w") as f:
            json.dump(data, f, indent=4)
            
    # Display their total dues of current month
    def monthly_dues(self):
        with open("Monthly_WT.json") as f:
            monthly_dues_json=json.load(f)
        
        # Extract just [Monthly Dues]
        for due in monthly_dues_json.values():
        # At index 2 bills are stored
            due_data = due[2]
            if "Monthly Dues" in due_data:
                self.M_previous_dues=due_data["Monthly Dues"]
        
        return self.M_previous_dues 
            
    def payment(self):
        if self.status == "Absent":
            self.bill = 0
            self.paid = 0
            self.dues = 0
        else:
            self.status = "Present"
            self.bill = self.can_price + self.cooler_price + self.drum_price
            self.paid = int(input("How much did you pay today? "))
            if not self.bill==0:
                self.dues = self.bill - self.paid
            else:                
                self.dues = 0
        
        return {
            "Today Bill": self.bill,
            "Today Paid": self.paid,
            "Today Dues": abs(self.dues)
        }
        
    def calculations(self, cans, cooler, drum):
        data = self.reading()
        self.can_price = cans * 20
        self.cooler_price = cooler * 10
        self.drum_price = drum * 20
        payment_details = self.payment()
        self.quantity={
            "Cans":cans,
            "Cooler":cooler,
            "Drum":drum
        }
        self.info = {
            "Date": self.current_date,
            "Attendance": self.status
        }
        self.price = {
            "Can Bill": self.can_price,
            "Cooler Bill": self.cooler_price,
            "Drum Bill": self.drum_price
        }
        
        # prepared dic to store in nice format
        id =self.get_next_id()
        data[id] = [self.info, self.quantity, self.price, payment_details]
        while id in data:
            id = random.randint(1, 999)
        # save into json
        self.storing(data)  
        
        # Send Data to API
        send=Upload_Daily_sheet_WT()
        send.send_daily_data(self.current_date,self.status,cans,cooler,drum,self.can_price,self.cooler_price,self.drum_price,self.bill,self.paid,self.dues)
        
        # Store monthly,yearly
        
        send=Monthly_History()
        yearly=Store_History()
        # When water vendor is present only then the data is stored in month adn yearly as well as data upload
        if self.ask_h=="y":
            send.monthly_values()
            # store yearly
            yearly.yearly_values()

            # call monthly data function to upload data after executing daily values
            send.send_monthly_data()

            # call yearly data function to upload data after executing monthly values
            yearly.send_yearly_data()
        
        
        
        
        

screen = Testing()
screen.Main_Screen()

# history_screen=Store_History()
# history_screen.monthly_values()
