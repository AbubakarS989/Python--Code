from datetime import datetime
import os, json

class Store_History:
    def __init__(self):
        self.current_date = datetime.now().strftime("%d-%m-%Y")
        self.current_month = datetime.now().strftime("%Y-%m")
        
        # Yearly Quantity
        self.yearly_cans = 0
        self.yearly_coolers = 0
        self.yearly_drums = 0

        self.yearly_bill = 0
        self.yearly_paid = 0
        self.yearly_dues = 0
        self.yearly_json = {}
        self.yearly_data = {}

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

    def reading_yearly_json(self):
        try:
            if os.path.exists("Entire_data_WT.json"):
                with open("Entire_data_WT.json", "r") as f:
                    self.yearly_json = json.load(f)
            else:
                self.yearly_json = {}
            return self.yearly_json
        except (IOError, json.JSONDecodeError) as e:
            print("Failed to load file:", e)
            self.yearly_json = {}
        return self.yearly_json

    def storing(self, data):
        with open("Entire_data_WT.json", "w") as f:
            json.dump(data, f, indent=4)

    def get_next_id(self):
        if self.yearly_json:
            last_id = max(self.yearly_json.keys(), key=int)
            return int(last_id) + 1
        else:
            return 1

    def yearly_values(self):
        # Extracting Quantities to calculate yearly calculations
        json_data = self.reading_json()
        
        for entry in json_data.values():
            # At index 1 quantities are stored
            quantity = entry[1]
            if "Cans" in quantity:
                self.yearly_cans += quantity["Cans"]
            if "Cooler" in quantity:
                self.yearly_coolers += quantity["Cooler"]
            if "Drum" in quantity:
                self.yearly_drums += quantity["Drum"]
            # At index 2 bills are stored
            bill_data = entry[3]
            print(bill_data)
            if "Today Bill" in bill_data:
                self.yearly_bill += bill_data["Today Bill"]
            if "Today Paid" in bill_data:
                self.yearly_paid += bill_data["Today Paid"]
            if "Today Dues" in bill_data:
                self.yearly_dues += bill_data["Today Dues"]
            
            self.yearly_dues = abs(self.yearly_bill - self.yearly_paid)
        
        yearly_quantity = {
            "Yearly Cans": self.yearly_cans,
            "Yearly Coolers": self.yearly_coolers,
            "Yearly Drums": self.yearly_drums
        }
        
        yearly_bill = {
            "Yearly Bill": self.yearly_bill,
            "Yearly Paid": self.yearly_paid,
            "Yearly Dues": self.yearly_dues
        }
        
        # uncomment to check
        # print(f"Yearly Cans: {self.yearly_cans}")
        # print(f"Yearly Coolers: {self.yearly_coolers}")
        # print(f"Yearly Drums: {self.yearly_drums}")
        # print(f"Yearly Bill: {self.yearly_bill}")
        # print(f"Yearly Paid: {self.yearly_paid}")
        # print(f"Yearly Dues: {self.yearly_dues}")

        id = self.get_next_id()
        # print(id)
        self.yearly_data[id] = [self.current_date, yearly_quantity, yearly_bill]
        self.storing(self.yearly_data)
    
    # to display specific month history in a json format
    def show_yearly_history_json_format(self, year):
    
        json_data = self.reading_json()
        yearly_entries = {k: v for k, v in json_data.items() if datetime.strptime(v[0]["Date"], "%d-%m-%Y").strftime("%Y") == year}

        # Check if the specified year exists in the data
        if yearly_entries:
            # Print the history for the specified year
            print(f"History for {year}:")
            # Convert the yearly data to a formatted JSON string and print it
            print(json.dumps(yearly_entries, indent=4))
        else:
            print(f"No data available for {year}")

if __name__=="__main__":
    screen = Store_History()
    screen.yearly_values()
    # screen.show_yearly_history_json_format(year="2024")
