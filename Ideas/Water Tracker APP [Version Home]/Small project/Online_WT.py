import json,os 
from datetime import datetime

class Upload_Data_sheet_WT:
    
    
    def __init__(self):
        self.current_data=datetime.now().strftime("%d-%m-%Y")
    


    def send_daily_data_(self):
        # Date
        # Attendence
        # Cans
        # Cooler
        # Drum 
        # Cans Price
        # Cooler Price 
        # Drum Price	
        # Total Bill
        # Bill Paid 	
        # Dues 				
      												
        print(self.current_data)




if __name__=="__main__":
    screen=Upload_Data_sheet_WT()
    screen.send_data_()

