

import requests
import json,os , random
from datetime import datetime
from colorama import init, Fore, Back, Style
from  history import History_WT_CWA
from common import HEAD
head=HEAD()
# initialize the colorama module
init()

class Water_Tracker_CWA:
    def __init__(self):
        self.Pixel_endpoint=""
        self.Sheety_endpoint=""
        self.current_date=datetime.now().strftime("%d-%m-%Y")
        
        # paid or not
        self.get=0
        # buy ot not
        self.ask=0
        
        self.can_price=20
        self.cooler_price=10
        self.Drum_can_price=20
        
        self.cans = 0
        self.cooler = 0
        self.drum = 0
        self.ID = 0
        self.status = ""
        
        self.Total_Bill=0
        self.paid_bill=0
        self.Dues=0
        
        self.can_bill=0
        self.drum_bill=0
        self.cooler_bill=0
        
        self.total_cans=0
        self.total_cooler=0
        self.total_drum=0
        
        self.grand_total_bill=0
        self.grand_total_paid=0
        self.grand_total_dues=0
        
        self.extract_data=0
        
        self.Monthly_Cans=0
        self.Monthly_Coolers=0
        self.Monthly_Drum=0
        
        self.Monthly_Bill=0
        self.Monthly_Paid=0
        self.Monthly_Dues=0
        
        
    def Home_Screen(self):
        #display header  
        head.header(heading=None)
        
        # Getting value from the user
        print("1: Enter Water Track")
        print("2: Show Water History ")
        print("3: Exit ")
        ask=input("Enter your choice:")
        try:
            ask=int(ask)
            if ask==1:
                self.input_screen()
            elif ask==2:
                History_screen=History_WT_CWA()
                History_screen.History()
            elif ask==3:
                print("Closing the program....")
                exit()
            else:
                print("Invalid input ")
        except ValueError as e:
            print("Invalid input ",e)
            

    def input_screen(self):
        
        # displaying header
        head.header(heading="Input Screen")
        
        # Did you buy water today?
        # Number of cans buy today? 
        # Number of cooler buy today? 
        # Number of Cans for [Drum] buy today? 
        # Did you paid the Bill? [yes / NO]
        #     How much you paid today?
        if not os.path.exists("data.json") :
            with open("data.json", 'w') as f:
              self.combine_list= json.dump({},f)

        with open("data.json", "r") as f:
            self.combine_list=json.load(f)
            
        
       
        self.ask=input(" Did you buy water today? [y/n]?")
        if self.ask=="y":
            self.cans=int(input(f"Enter Quantity of {Fore.BLUE}Can{Style.RESET_ALL} you buy today: ?"))
            self.cooler=int(input(f"Enter Quantity of {Fore.GREEN}Cooler{Style.RESET_ALL} you buy today?: "))
            self.drum=int(input(f"Enter Quantity of {Fore.CYAN}Drum Cans{Style.RESET_ALL} you buy today?: "))
            self.get=input("Did you Paid the Bill? [y/n]").lower()
            
            if self.get=="y":
                self.paid_bill=int(input("How much you paid today? [Rupees]"))
            elif self.get=="n":
                self.paid_bill=0

            self.status="Present"
        elif self.ask=="n":
            # if the user didn't buy, then values are assigned zero automatically
            self.cans=self.cooler=self.drum=0
            self.status="Absent"

           
        # Assign the next increment id to each entry
        if self.combine_list:
            self.ID = max(map(int, self.combine_list.keys())) + 1
        else:
            self.ID = 1
        
        # Call the method to store data
        self.Storing()     
        
    def Storing(self):
        
        
        # Store each quantity into dic
        
        self.calculations()
        quantity={
            "Date":self.current_date,
            "Cans":self.cans,
            "Cooler":self.cooler,
            "Drum":self.drum
            }
        billing_info={
            "Total Bill":self.Total_Bill,
            "Paid Bill ":self.paid_bill,
            "Dues":self.Dues
        }
        Price={
            "Cans Bill":self.can_bill,
            "Coolers Bill":self.cooler_bill,
            "Drum Bill":self.drum_bill
        }
     
        Bill_History={
        "Monthly Cans":self.Monthly_Cans,
        "Total Cans":self.total_cans,
        "Monthly Coolers":self.Monthly_Coolers,
        "Total Coolers":self.total_cooler,
        "Monthly Drum":self.Monthly_Drum,
        "Total Drum":self.total_drum,
        "Monthly Bill":self.Monthly_Bill,
        "Monthly Paid":self.Monthly_Paid,
        "Monthly Dues":self.Monthly_Dues,
        "Grand_Total_Bill":self.grand_total_bill,
        "Grand_Total_Paid":self.grand_total_paid
        
            
            
        }
        Total_Entries=[[self.status],[quantity],[Price],[billing_info],[Bill_History]]
        self.combine_list[self.ID]=Total_Entries
        # print(self.combine_list)
        
        try:
            with open("data.json","w") as f:
                json.dump(self.combine_list,f,indent=4)
        except Exception as e:
            print("Error",e)
        
        
        
            
            
        
        
        
    def calculations(self):
        lst_dates=[]
        # Individual bill of each day
        self.can_bill=self.cans*self.can_price
        self.cooler_bill=self.cooler*self.cooler_price
        self.drum_bill=self.drum*self.Drum_can_price
        self.Total_Bill=self.can_bill+self.cooler_bill+self.drum_bill
        print(self.Total_Bill)
        
        
           
        # Extracting data from the file for grand values and monthly values
        if not os.path.exists("data.json"):
            with open("data.json", 'w') as f:
                json.dump({}, f)
        
        with open("data.json", "r") as f:
            self.combine_list = json.load(f)
            
        for entry in self.combine_list.values():
            
            quantity = entry[1][0]  # Quantity is at index 1, and it's the first item in the list
            billing_info = entry[3][0]  # Billing info is at index 3, and it's the first item in the list
            bill_history = entry[4][0]  # Bill history is at index 4, and it's the first item in the list
            # if user buy a water then  calculations could perform
            if self.ask=="y":
            # Extract quantity of data
                if "Cans" in quantity:    
                    self.total_cans+= quantity["Cans"]
                if "Cooler":
                    self.total_cooler+= quantity["Cooler"]
                if "Drum":
                    self.total_drum+= quantity["Drum"]
                if "Date" in quantity:
                    lst_dates.append(quantity["Date"])
                
            # Extract Data  Of Grand Values

                if "Total Bill" in billing_info:
                    self.Total_Bill += billing_info["Total Bill"]
                    
                if "Total Bill" in billing_info:
                    self.grand_total_bill += billing_info["Total Bill"]
            # if user didn't buy a water then  calculations could perform
            
            if self.ask=="n":        
                if "Cans" in quantity:    
                    self.total_cans= quantity["Cans"]c 8
                if "Cooler":
                    self.total_cooler= quantity["Cooler"]
                if "Drum":
                    self.total_drum= quantity["Drum"]
                if "Date" in quantity:
                    lst_dates.append(quantity["Date"])

                if "Total Bill" in billing_info:
                    self.Total_Bill = billing_info["Total Bill"]
                    
                if "Grand_Total_Bill" in bill_history:
                    self.grand_total_bill = billing_info["Grand_Total_Bill"]
                    
            # if user paid the bill then  calculations could perform
            if self.get=="y":
                if "Paid Bill " in billing_info:
                    self.grand_total_bill += billing_info["Paid Bill "]
                # Extract Data  Of Current bills
                if "Paid Bill " in billing_info:
                    self.paid_bill += billing_info["Paid Bill "]
                    
            if self.get=="n":
                if "Dues" in billing_info:
                    self.Dues = billing_info["Dues"]
                    
                if "Paid Bill " in billing_info:
                    self.grand_total_bill += billing_info["Paid Bill "]
                    
        # Individual daily values
        self.total_cans+= self.cans
        self.total_cooler+=self.cooler
        self.total_drum+=self.drum
                
                
                
        self.Dues=self.Total_Bill-self.paid_bill
        self.grand_total_bill+=self.Total_Bill
        self.grand_total_paid+=self.paid_bill
        self.grand_total_dues+=self.Dues
        
        
        # Grand Values
        # strip_date=[] 
        # for i in lst_dates:
        #     # print(type(i)) #String
        #     strip_date.append(datetime.strptime(i,"%d-%m-%Y").strftime("%d%m%Y"))
            
        # print(strip_date)
        
        # Monthly Data
        if not os.path.exists("data.json"):
            with open("data.json", 'w') as f:
                json.dump({}, f)
        
        with open("data.json", "r") as f:
            self.combine_list = json.load(f)
        # date_lst = []
        # for date in strip_date:
        #     day = date[0:2]
        #     month = f"{date[2:4]}"
        #     year = f"{date[4:8]}"
        #     date_lst.append([day,month, year])
        # Helper function to parse date strings
            
        # today = datetime.now()  # Today’s date
        # start_of_current_month = today.replace(day=1)  # First day of this month
        # start_of_last_month = (start_of_current_month - timedelta(days=1)).replace(day=1)  # First day of last month
        # end_of_last_month = start_of_current_month - timedelta(days=1)  # Last day of last month
       
        
        # for entry in combine_list.values():
        #     date_str = entry[1][0]['Date']  # Date from the entry
        #     quantity = entry[1][0]  # Quantity is at index 1, and it's the first item in the list
        # entry_date = self.parse_date(date_str)  # Convert date string to date object

        #     if start_of_last_month <= entry_date <= end_of_last_month:
        #         # Add up the values if the date is within the last month
        #         if "Cans" in quantity:    
        #             self.Monthly_Cans += bill_history["Cans"]
        #         if "Cooler":
        #             self.Monthly_Coolers += bill_history["Monthly Cooler"]
        #         if "Drum":
        #             self.Monthly_Drum += bill_history["Drum"]



        # print(date_dict)
        
         

        
        
    def parse_date(date_str):
        
        return datetime.strptime(date_str, "%d%m%Y")
    def output_screen(self):
        
        head.header(heading="Output Screen")
        print("from output screen")
        
        
        


    
   
    
        
        
        
        
        
        
# screen=Water_Tracker_CWA()        
# screen.Home_Screen()
# screen.input_screen()
if __name__=="__main__":
    
    screen=Water_Tracker_CWA()        
    screen.Home_Screen()
    input("Press Enter to exit.")

    


