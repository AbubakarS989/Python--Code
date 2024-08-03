from datetime import datetime
import os, json
from Online_WT import Upload_monthly_sheet_WT

class Monthly_History:
    def __init__(self):
        self.current_date = datetime.now().strftime("%d-%m-%Y")
        self.current_month = datetime.now().strftime("%Y-%m")
        # Monthly Quantity
        self.monthly_cans = 0
        self.monthly_coolers = 0
        self.monthly_drums = 0

        self.monthly_bill = 0
        self.monthly_paid = 0
        self.monthly_dues = 0
        self.send_data=Upload_monthly_sheet_WT()
        

    def reading_json(self):
        try:
            if os.path.exists("Daily_data_WT.json"):
                with open("Daily_data_WT.json", "r") as f:
                    self.data = json.load(f)
            else:
                self.data = {}
            return self.data
        except (IOError, json.JSONDecodeError) as e:
            print("Failed to load file:", e)
        return {}

    def reading_monthly_json(self):
        try:
            if os.path.exists("Monthly_WT.json"):
                with open("Monthly_WT.json", "r") as f:
                    self.Monthly_json = json.load(f)
            else:
                self.Monthly_json = {}
            return self.Monthly_json
        except (IOError, json.JSONDecodeError) as e:
            print("Failed to load file:", e)
            self.Monthly_json = {}
        return self.Monthly_json

    def storing(self, data):
        with open("Monthly_WT.json", "w") as f:
            json.dump(data, f, indent=4)

    def get_next_id(self):
        if self.Monthly_json:
            last_id = max(self.Monthly_json.keys(), key=int)
            return int(last_id) + 1
        else:
            return 1

    def monthly_values(self):
        # Extracting Quantities to calculate monthly calculations
        json_data = self.reading_json()
        Monthly_data = self.reading_monthly_json()
        for entry in json_data.values():
            entry_date = datetime.strptime(entry[0]["Date"], "%d-%m-%Y").strftime("%Y-%m")
            if entry_date != self.current_month:
                    continue
                
            # At index 1 quantities are stored
            quantity = entry[1]

            if "Cans" in quantity:
                self.monthly_cans += quantity["Cans"]
            if "Cooler" in quantity:
                self.monthly_coolers += quantity["Cooler"]
            if "Drum" in quantity:
                self.monthly_drums += quantity["Drum"]

        for entry in json_data.values():
            entry_date = datetime.strptime(entry[0]["Date"], "%d-%m-%Y").strftime("%Y-%m")
            if entry_date != self.current_month:
                    continue
                
            # At index 2 bills are stored
            bill_data = entry[3]
            # print(bill_data)
            if "Today Bill" in bill_data:
                self.monthly_bill += bill_data["Today Bill"]
            if "Today Paid" in bill_data:
                self.monthly_paid += bill_data["Today Paid"]
            if "Today Dues" in bill_data:
                self.monthly_dues += bill_data["Today Dues"]
            
            self.monthly_dues=abs(self.monthly_bill-self.monthly_paid)
            
        
        monthly_quantity = {
            "Monthly Cans": self.monthly_cans,
            "Monthly Cooler": self.monthly_coolers,
            "Monthly Drum": self.monthly_drums
        }
        
        
        monthly_bill = {
            "Monthly Bill": self.monthly_bill,
            "Monthly Paid": self.monthly_paid,
            "Monthly Dues": self.monthly_dues
        }
        
        
        id = self.get_next_id()
        Monthly_data[id] = [self.current_date,monthly_quantity, monthly_bill]
        self.storing(Monthly_data)
        
    def send_monthly_data(self):
        
        #? Reuse this code bcz, i want to call this function after executing the daily values in [main.py], so the monthly bill is prepared, to send that prepared bill, I wanna get the data first from the file and then upload it into drive
        monthly_can=0
        monthly_cooler=0
        monthly_drum=0
        monthly_bill=0
        monthly_paid=0
        monthly_dues=0
        
        
        
        
        Monthly_data = self.reading_monthly_json()
        
        for entry in Monthly_data.values():        
            # At index 1 quantities are stored
            quantity = entry[1]

            if "Monthly Cans" in quantity:
                monthly_can = quantity["Monthly Cans"]
            if "Monthly Cooler" in quantity:
                monthly_cooler = quantity["Monthly Cooler"]
            if "Monthly Drum" in quantity:
                monthly_drum = quantity["Monthly Drum"]
                
            # At index 2 bills are stored
            bill_data = entry[2]
            # print(bill_data)
            if "Monthly Bill" in bill_data:
                monthly_bill = bill_data["Monthly Bill"]
            if "Monthly Paid" in bill_data:
                monthly_paid = bill_data["Monthly Paid"]
            if "Monthly Dues" in bill_data:
                monthly_dues = bill_data["Monthly Dues"]
                
        # call func to send monthly values
        
        self.send_data.send_monthly_data(self.current_date,monthly_can,monthly_cooler,monthly_drum,monthly_bill,monthly_paid,monthly_dues)
        
    def display_monthly_values(self):
        #? Reuse this code bcz, i wanna display  each month history separated  to the user without send data to api as i did above
                
        
        Monthly_data = self.reading_monthly_json()
        separated_month_history={}
        
        for entry in Monthly_data.values():
            entry_date=datetime.strptime(entry[0],"%d-%m-%Y").strftime("%Y-%m")
            
            Monthly_quantity=entry[1]
            Monthly_bills=entry[2]
            
            # initialize all values zero if data is not found
            if entry_date not in separated_month_history:
                separated_month_history[entry_date]={
                    "Cans":0,
                    "Cooler":0,
                    "Drum":0,
                    "Bill":0,
                    "Paid":0,
                    "Dues":0
                }

            # store entire month history of each month separately into dic 
            separated_month_history[entry_date]["Cans"]=Monthly_quantity["Monthly Cans"]
            separated_month_history[entry_date]["Cooler"]=Monthly_quantity["Monthly Cooler"]
            separated_month_history[entry_date]["Drum"]=Monthly_quantity["Monthly Drum"]
            separated_month_history[entry_date]["Bill"]=Monthly_bills["Monthly Bill"]
            separated_month_history[entry_date]["Paid"]=Monthly_bills["Monthly Paid"]
            separated_month_history[entry_date]["Dues"]=Monthly_bills["Monthly Dues"]
         
                
        
        print(f"\n---------------  Water Tracker [Home Version]   -------------------")
        print(f"---------------         Monthly History             ---------------")
        print(f"--------------       Code With Abubakar              --------------\n")
        
        
        # now loop through the dic and print all months values
        
        for month, data in separated_month_history.items():
            print(f"Month: {month}")
            print(f"  Cans: {data['Cans']}")
            print(f"  Cooler: {data['Cooler']}")
            print(f"  Drum: {data['Drum']}")
            print(f"  Bill: {data['Bill']}")
            print(f"  Paid: {data['Paid']}")
            print(f"  Dues: {data['Dues']}")
            

    # to display specific month history in a json format
    def show_monthly_history_json_format(self, month):
        
        json_data = self.reading_json()
        monthly_entries = {k: v for k, v in json_data.items() if datetime.strptime(v[0]["Date"], "%d-%m-%Y").strftime("%Y-%m") == month}

        # Check if the specified month exists in the monthly data
        if monthly_entries:
            
            print(f"History for {month}:")
            # Convert the monthly data to a formatted JSON string and print it
            print(json.dumps(monthly_entries, indent=4))
        else:
            # Print a message if no data is available for the specified month
            print(f"No data available for {month}")

if __name__ == "__main__":
    screen = Monthly_History()
    # screen.monthly_values()
    screen.display_monthly_values()
    # screen.show_monthly_history_json_format(screen.current_month)
