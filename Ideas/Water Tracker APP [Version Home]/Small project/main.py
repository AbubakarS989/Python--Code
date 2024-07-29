from datetime import datetime
import os, json, random


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
    
    def home_screen(self):
        ask = input("Did you buy [y/n]? ").lower()
        if ask == "y":
            print("Welcome to tracker testing\n")
            can = int(input("Enter cans: "))
            cooler = int(input("Enter cooler: "))
            drum = int(input("Enter drum: "))
            self.calculations(can, cooler, drum)
            self.status = "Present"
        elif ask == "n":
            self.status = "Absent"
            self.calculations(cans=0, cooler=0, drum=0)
    
    def reading(self):
        try:
            if os.path.exists("Testing.json"):
                with open("Testing.json", "r") as f:
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
        with open("Testing.json", "w") as f:
            json.dump(data, f, indent=4)
            
    def payment(self):
        if self.status == "Absent":
            self.bill = 0
            self.paid = 0
            self.dues = 0
        else:
            self.status = "Present"
            self.bill = self.can_price + self.cooler_price + self.drum_price
            self.paid = int(input("How much did you pay today? "))
            self.dues = self.bill - self.paid
        
        return {
            "Today Bill": self.bill,
            "Today Paid": self.paid,
            "Today Dues": self.dues
        }
        
    def calculations(self, cans, cooler, drum):
        data = self.reading()
        self.can_price = cans * 20
        self.cooler_price = cooler * 10
        self.drum_price = drum * 20
        payment_details = self.payment()
        
        self.info = {
            "Date": self.current_date,
            "Attendance": self.status
        }
        self.price = {
            "Can Bill": self.can_price,
            "Cooler Bill": self.cooler_price,
            "Drum Bill": self.drum_price
        }
        
        id =self.get_next_id()
        data[id] = [self.info, self.price, payment_details]
        while id in data:
            id = random.randint(1, 999)
        
        print(data)
        self.storing(data)

screen = Testing()
screen.home_screen()
