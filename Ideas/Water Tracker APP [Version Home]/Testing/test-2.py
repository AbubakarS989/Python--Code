import json
import os
from datetime import datetime

DATA_FILE = 'water_data.json'

class WaterTracker:
    def __init__(self, data_file):
        self.data_file = data_file
        self.data = self.read_json()
        self.previous_dues = self.calculate_previous_dues()
        self.next_id = self.get_next_id()

    def read_json(self):
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            return {}
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error reading JSON file: {e}")
            return {}

    def write_json(self):
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.data, file, indent=4)
        except IOError as e:
            print(f"Error writing to JSON file: {e}")

    def calculate_previous_dues(self):
        try:
            if self.data:
                last_entry_id = max(self.data.keys(), key=int)
                last_entry = self.data[str(last_entry_id)]
                if len(last_entry) > 3:
                    previous_dues = last_entry[4][0].get("Grand_Total_Dues", 0)
                    return previous_dues
            return 0
        except (IndexError, KeyError) as e:
            print(f"Error calculating previous dues: {e}")
            return 0

    def get_next_id(self):
        if self.data:
            last_id = max(self.data.keys(), key=int)
            return int(last_id) + 1
        return 1

    def prompt_user(self):
        try:
            buy_water_today = input("Did you buy water today? (yes/no): ").strip().lower()
            if buy_water_today == 'no':
                self.handle_no_purchase()
            elif buy_water_today == 'yes':
                self.collect_data()
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def handle_no_purchase(self):
        try:
            print(f"Previous Dues: {self.previous_dues}")
            bill_paid_today = input("Did you pay for previous dues today? (yes/no): ").strip().lower()
            if bill_paid_today == 'yes':
                amount_paid = float(input("Enter the amount paid towards previous dues: ").strip())
                if amount_paid > self.previous_dues:
                    print("Error: Payment amount exceeds previous dues.")
                    return
                today_paid_bill = amount_paid
                today_dues = self.previous_dues - amount_paid
            elif bill_paid_today == 'no':
                today_paid_bill = 0
                today_dues = self.previous_dues
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                return

            # Prepare data to store in JSON
            current_date = datetime.now().strftime("%Y-%m-%d")
            new_entry = [
                ["Present"],
                [{
                    "Date": current_date,
                    "Cans": 0,
                    "Cooler": 0,
                    "Drum": 0,
                }],
                [{}],
                [{
                    "Today Total Bill": 0,
                    "Today Paid Bill": today_paid_bill,
                    "Today Dues": today_dues,
                }],
                [{
                    "Monthly Cans": 0,
                    "Total Cans": 0,
                    "Monthly Coolers": 0,
                    "Total Coolers": 0,
                    "Monthly Drum": 0,
                    "Total Drum": 0,
                    "Grand_Total_Bill": self.get_grand_total("Grand_Total_Bill") + 0,
                    "Grand_Total_Paid": self.get_grand_total("Grand_Total_Paid") + today_paid_bill,
                    "Grand_Total_Dues": self.get_grand_total("Grand_Total_Dues") + today_dues,
                }]
            ]
            self.data[str(self.next_id)] = new_entry
            self.next_id += 1

            # Save data to JSON
            self.write_json()
            print("Data saved successfully.")
        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def collect_data(self):
        try:
            quantity_cans = int(input("Enter the Quantity of Water Cans you bought today: ").strip())
            quantity_coolers = int(input("Enter the Quantity of Water Coolers you bought today: ").strip())
            quantity_drums = int(input("Enter the Quantity of Water Drums you bought today: ").strip())

            # Assuming some pricing
            price_per_can = 5
            price_per_cooler = 20
            price_per_drum = 50

            total_bill = (quantity_cans * price_per_can) + (quantity_coolers * price_per_cooler) + (quantity_drums * price_per_drum)

            print(f"Total Bill: {total_bill}")
            print(f"Previous Dues: {self.previous_dues}")

            bill_paid_today = input("Did you pay the bill today? (yes/no): ").strip().lower()
            if bill_paid_today == 'yes':
                amount_paid = float(input("Enter the amount paid today: ").strip())
                if amount_paid > total_bill:
                    print("Error: Payment amount exceeds the total bill.")
                    return
                today_paid_bill = amount_paid
                today_dues = total_bill - amount_paid
            elif bill_paid_today == 'no':
                today_paid_bill = 0
                today_dues = total_bill
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                return

            # Update previous dues
            self.previous_dues += today_dues

            # Prepare data to store in JSON
            current_date = datetime.now().strftime("%Y-%m-%d")
            new_entry = [
                ["Present"],
                [{
                    "Date": current_date,
                    "Cans": quantity_cans,
                    "Cooler": quantity_coolers,
                    "Drum": quantity_drums,
                }],
                [{
                    "Cans Bill": quantity_cans * price_per_can,
                    "Cooler Bill": quantity_coolers * price_per_cooler,
                    "Drum Bill": quantity_drums * price_per_drum,
                }],
                [{
                    "Today Total Bill": total_bill,
                    "Today Paid Bill": today_paid_bill,
                    "Today Dues": today_dues,
                }],
                [{
                    "Monthly Cans": quantity_cans,
                    "Total Cans": quantity_cans,
                    "Monthly Coolers": quantity_coolers,
                    "Total Coolers": quantity_coolers,
                    "Monthly Drum": quantity_drums,
                    "Total Drum": quantity_drums,
                    "Grand_Total_Bill": self.get_grand_total("Grand_Total_Bill") + total_bill,
                    "Grand_Total_Paid": self.get_grand_total("Grand_Total_Paid") + today_paid_bill,
                    "Grand_Total_Dues": self.get_grand_total("Grand_Total_Dues") + today_dues,
                }]
            ]
            self.data[str(self.next_id)] = new_entry
            self.next_id += 1

            # Save data to JSON
            self.write_json()
            print("Data saved successfully.")
        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def get_grand_total(self, key):
        """Retrieve the grand total value from the most recent entry."""
        if self.data:
            last_entry_id = max(self.data.keys(), key=int)
            last_entry = self.data[str(last_entry_id)]
            if len(last_entry) > 4:
                return last_entry[4][0].get(key, 0)
        return 0

if __name__ == '__main__':
    tracker = WaterTracker(DATA_FILE)
    tracker.prompt_user()
