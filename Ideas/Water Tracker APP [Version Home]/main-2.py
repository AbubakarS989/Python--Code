import os
import json
from datetime import datetime

class WaterBilling:
    def __init__(self):
        self.current_date = datetime.now().strftime("%d-%m-%Y")
        self.combine_list = self.load_data()
        
        # Initialize all necessary variables
        self.total_cans = 0
        self.total_cooler = 0
        self.total_drum = 0
        self.grand_total_bill = 0
        self.grand_total_paid = 0
        self.grand_total_dues = 0
        self.previous_dues = 0
        
        self.can_price = 20  # Example prices, adjust as needed
        self.cooler_price = 10
        self.drum_can_price = 20

        # Initialize monthly values
        self.Monthly_Cans = 0
        self.Monthly_Coolers = 0
        self.Monthly_Drum = 0
        self.Monthly_Bill = 0
        self.Monthly_Paid = 0
        self.Monthly_Dues = 0
        
    def load_data(self):
        if not os.path.exists("data.json"):
            with open("data.json", 'w') as f:
                json.dump({}, f)
        with open("data.json", "r") as f:
            return json.load(f)
    
    def get_input(self):
        self.ask = input("Did you buy water today? [y/n]? ").lower()
        
        if self.ask == "y":
            self.status = "Present"
            self.cans = int(input("Enter Quantity of Can you bought today: "))
            self.cooler = int(input("Enter Quantity of Cooler you bought today: "))
            self.drum = int(input("Enter Quantity of Drum Cans you bought today: "))
            self.get = input("Did you pay the Bill? [y/n] ").lower()
            
            if self.get == "y":
                self.paid_bill = int(input("How much did you pay today? [Rupees] "))
            else:
                self.paid_bill = 0
        elif self.ask == "n":
            self.status = "Absent"
            self.cans = 0
            self.cooler = 0
            self.drum = 0
            self.paid_bill = 0
        else:
            print("Select a valid option.")
            return
        
        # Assign the next increment ID to each entry
        if self.combine_list:
            self.ID = max(map(int, self.combine_list.keys())) + 1
        else:
            self.ID = 1
        
        self.storing()

    def calculations(self):
        # Individual bill of each day
        self.can_bill = self.cans * self.can_price
        self.cooler_bill = self.cooler * self.cooler_price
        self.drum_bill = self.drum * self.drum_can_price
        self.Total_Bill = self.can_bill + self.cooler_bill + self.drum_bill
        self.Dues = self.Total_Bill - self.paid_bill

        # Update monthly values
        self.Monthly_Cans += self.cans
        self.Monthly_Coolers += self.cooler
        self.Monthly_Drum += self.drum
        self.Monthly_Bill += self.Total_Bill
        self.Monthly_Paid += self.paid_bill
        self.Monthly_Dues += self.Dues

        # Extract data from the JSON file for calculations
        for entry in self.combine_list.values():
            quantity = entry[1][0]
            billing_info = entry[3][0]
            bill_history = entry[4][0]
            
            if self.ask == "y":
                if "Cans" in quantity:
                    self.total_cans += quantity["Cans"]
                if "Cooler" in quantity:
                    self.total_cooler += quantity["Cooler"]
                if "Drum" in quantity:
                    self.total_drum += quantity["Drum"]
                if "Total Bill" in billing_info:
                    self.grand_total_bill += billing_info["Total Bill"]
                if self.get == "y" and self.Total_Bill == 0 and "Dues" in billing_info:
                    self.previous_dues += abs(billing_info["Dues"] - self.paid_bill)
            elif self.get == "y":
                if "Paid Bill " in billing_info:
                    self.grand_total_bill += billing_info["Paid Bill "]
                    self.paid_bill += billing_info["Paid Bill "]
                self.Dues = abs(self.Total_Bill - self.paid_bill - self.previous_dues)
            elif self.get == "n":
                if "Dues" in billing_info:
                    self.Dues += billing_info["Dues"]

        self.total_cans += self.cans
        self.total_cooler += self.cooler
        self.total_drum += self.drum

        self.grand_total_bill += self.Total_Bill
        self.grand_total_paid += self.paid_bill
        self.grand_total_dues += self.Dues

    def storing(self):
        self.calculations()

        quantity = {
            "Date": self.current_date,
            "Cans": self.cans,
            "Cooler": self.cooler,
            "Drum": self.drum
        }
        billing_info = {
            "Total Bill": self.Total_Bill,
            "Paid Bill ": self.paid_bill,
            "Dues": self.Dues
        }
        price = {
            "Cans Bill": self.can_bill,
            "Coolers Bill": self.cooler_bill,
            "Drum Bill": self.drum_bill
        }
        bill_history = {
            "Monthly Cans": self.Monthly_Cans,
            "Total Cans": self.total_cans,
            "Monthly Coolers": self.Monthly_Coolers,
            "Total Coolers": self.total_cooler,
            "Monthly Drum": self.Monthly_Drum,
            "Total Drum": self.total_drum,
            "Monthly Bill": self.Monthly_Bill,
            "Monthly Paid": self.Monthly_Paid,
            "Monthly Dues": self.Monthly_Dues,
            "Grand_Total_Bill": self.grand_total_bill,
            "Grand_Total_Paid": self.grand_total_paid,
            "Grand_Total_Dues": self.grand_total_dues
        }

        total_entries = [[self.status], [quantity], [price], [billing_info], [bill_history]]
        self.combine_list[self.ID] = total_entries

        try:
            with open("data.json", "w") as f:
                json.dump(self.combine_list, f, indent=4)
        except Exception as e:
            print("Error:", e)

    def view_monthly_history(self):
        # Display monthly history
        print("\nMonthly History:")
        print("------------------------------------------------")
        for entry in self.combine_list.values():
            bill_history = entry[4][0]  # Bill history is at index 4, first item in the list
            print(f"Date: {bill_history.get('Date', 'N/A')}")
            print(f"Monthly Cans: {bill_history.get('Monthly Cans', 'N/A')}")
            print(f"Total Cans: {bill_history.get('Total Cans', 'N/A')}")
            print(f"Monthly Coolers: {bill_history.get('Monthly Coolers', 'N/A')}")
            print(f"Total Coolers: {bill_history.get('Total Coolers', 'N/A')}")
            print(f"Monthly Drum: {bill_history.get('Monthly Drum', 'N/A')}")
            print(f"Total Drum: {bill_history.get('Total Drum', 'N/A')}")
            print(f"Monthly Bill: {bill_history.get('Monthly Bill', 'N/A')}")
            print(f"Monthly Paid: {bill_history.get('Monthly Paid', 'N/A')}")
            print(f"Monthly Dues: {bill_history.get('Monthly Dues', 'N/A')}")
            print(f"Grand Total Bill: {bill_history.get('Grand_Total_Bill', 'N/A')}")
            print(f"Grand Total Paid: {bill_history.get('Grand_Total_Paid', 'N/A')}")
            print(f"Grand Total Dues: {bill_history.get('Grand_Total_Dues', 'N/A')}")
            print("------------------------------------------------\n")

# Usage example
if __name__ == "__main__":
    billing = WaterBilling()
    billing.get_input()
    billing.view_monthly_history()
