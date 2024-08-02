import json,os 
from datetime import datetime
# Separate file for sending data to sheety
from user_credentials_sheety_WT import daily_sheet_Api

class Upload_Daily_sheet_WT:
    
    
    def __init__(self):
        self.current_date=datetime.now().strftime("%d-%m-%Y")
    


    def send_daily_data(self,Date,Attendance,cans,cooler,drum,can_price,cooler_price,drum_price,Total_Bill,paid,Dues):
        
        # ? How data is store in a google sheet
        # {'dailyDataSheet': [{'date': 'rf', 'attendance': 'er', 'cans': 'ert', 'cooler': 'ert', 'drum': 'err', 'cansPrice': 'ret', 'coolerPrice': 'ert', 'drumPrice': 'ret', 'totalBill': 'ert', 'billPaid': 'ert', 'dues': 'er', 'id': 2}]} 
        
        print(paid)
        sheet_input={
            "dailyDataSheet":{
                "date": Date,
                "attendance": Attendance,
                "cans":cans,
                "cooler":cooler ,
                "drum":drum,
                "cansPrice":can_price,
                "coolerPrice":cooler_price,
                "drumPrice":drum_price,
                "totalBill":Total_Bill,
                "dues":Dues,
                "paidBill":paid,
            }
        }
        print(sheet_input)
        daily_sheet_Api(sheet_input=sheet_input)
    
        									
        print(self.current_date)



class Upload_monthly_sheet_WT(Upload_Daily_sheet_WT):
    def __init__(self):
        # initialize the parent class
        super().__init__()
        # self.current_date
    
    def send_monthly_data(self):
        print(self.current_date)
    
# if __name__=="__main__":
#     screen1=Upload_Daily_sheet_WT()
#     screen1.send_daily_data()
    # screen2=Upload_monthly_sheet_WT()
    # screen2.send_monthly_data()

