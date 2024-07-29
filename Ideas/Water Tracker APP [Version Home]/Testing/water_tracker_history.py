import json

DATA_FILE = 'water_data.json'

class WaterTrackerHistory:
    def __init__(self, data_file):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Data file not found.")
            return {}
        except json.JSONDecodeError:
            print("Error decoding JSON data.")
            return {}

    def display_monthly_history(self):
        monthly_totals = {}
        for entry_id, entry in self.data.items():
            if len(entry) > 4:
                monthly_data = entry[4][0]
                month = entry[1][0]["Date"][:7]  # Extract month from date
                if month not in monthly_totals:
                    monthly_totals[month] = {
                        "Monthly Cans": 0,
                        "Monthly Coolers": 0,
                        "Monthly Drum": 0,
                        "Monthly Bill": 0,
                        "Monthly Paid": 0,
                        "Monthly Dues": 0
                    }
                monthly_totals[month]["Monthly Cans"] += monthly_data.get("Monthly Cans", 0)
                monthly_totals[month]["Monthly Coolers"] += monthly_data.get("Monthly Coolers", 0)
                monthly_totals[month]["Monthly Drum"] += monthly_data.get("Monthly Drum", 0)
                monthly_totals[month]["Monthly Bill"] += monthly_data.get("Monthly Bill", 0)
                monthly_totals[month]["Monthly Paid"] += monthly_data.get("Monthly Paid", 0)
                monthly_totals[month]["Monthly Dues"] += monthly_data.get("Monthly Dues", 0)

        for month, totals in sorted(monthly_totals.items()):
            print(f"\n{month}:")
            for key, value in totals.items():
                print(f"  {key}: {value}")

    def display_entire_history(self):
        grand_totals = {
            "Total Cans": 0,
            "Total Coolers": 0,
            "Total Drum": 0,
            "Grand Total Bill": 0,
            "Grand Total Paid": 0,
            "Grand Total Dues": 0
        }
        
        for entry in self.data.values():
            if len(entry) > 4:
                grand_data = entry[4][0]
                grand_totals["Total Cans"] += grand_data.get("Total Cans", 0)
                grand_totals["Total Coolers"] += grand_data.get("Total Coolers", 0)
                grand_totals["Total Drum"] += grand_data.get("Total Drum", 0)
                grand_totals["Grand Total Bill"] += grand_data.get("Grand_Total_Bill", 0)
                grand_totals["Grand Total Paid"] += grand_data.get("Grand_Total_Paid", 0)
                grand_totals["Grand Total Dues"] += grand_data.get("Grand_Total_Dues", 0)

        print("\nGrand Totals:")
        for key, value in grand_totals.items():
            print(f"  {key}: {value}")

    def display_menu(self):
        while True:
            print("\nWater Tracker History")
            print("1: See Monthly History")
            print("2: See Entire History")
            print("3: Exit")
            choice = input("Your choice: ").strip()

            if choice == '1':
                self.display_monthly_history()
            elif choice == '2':
                self.display_entire_history()
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    history = WaterTrackerHistory(DATA_FILE)
    history.display_menu()
