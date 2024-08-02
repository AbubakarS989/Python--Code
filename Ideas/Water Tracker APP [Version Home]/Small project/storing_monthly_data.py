from datetime import datetime
import os, json


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
        
        # print(f"Monthly Cans: {self.monthly_cans}")
        # print(f"Monthly Coolers: {self.monthly_coolers}")
        # print(f"Monthly Drums: {self.monthly_drums}")
        # print(f"Monthly Bill: {self.monthly_bill}")
        # print(f"Monthly Paid: {self.monthly_paid}")
        # print(f"Monthly Dues: {self.monthly_dues}")
    
    # to display specific month history in a json format
    def show_monthly_history_jsonfm(self, month):
    
        json_data = self.reading_json()
        monthly_entries = {k: v for k, v in json_data.items() if datetime.strptime(v[0]["Date"], "%d-%m-%Y").strftime("%Y-%m") == month}

        # Check if the specified month exists in the monthly data
        if monthly_entries:
            # Print the history for the specified month
            print(f"History for {month}:")
            # Convert the monthly data to a formatted JSON string and print it
            print(json.dumps(monthly_entries, indent=4))
        else:
            # Print a message if no data is available for the specified month
            print(f"No data available for {month}")

if __name__ == "__main__":
    screen = Monthly_History()
    screen.monthly_values()
# screen.show_monthly_history_jsonfm(screen.current_month)
