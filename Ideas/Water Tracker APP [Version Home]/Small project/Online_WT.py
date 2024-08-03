import json
import os
from datetime import datetime
# Separate file for sending data on google sheets
from user_credentials_sheety_WT import daily_sheet_Api, monthly_sheet_Api, yearly_sheet_Api


class Upload_Daily_sheet_WT:

    def __init__(self):
        self.current_date = datetime.now().strftime("%d-%m-%Y")

    def send_daily_data(self, Date, Attendance, cans, cooler, drum, can_price, cooler_price, drum_price, Total_Bill, paid, Dues):

        # ? How data is store in a google sheet
        # {'dailyDataSheet': [{'date': 'rf', 'attendance': 'er', 'cans': 'ert', 'cooler': 'ert', 'drum': 'err', 'cansPrice': 'ret', 'coolerPrice': 'ert', 'drumPrice': 'ret', 'totalBill': 'ert', 'billPaid': 'ert', 'dues': 'er', 'id': 2}]}

        sheet_input = {
            "dailyDataSheet": {
                "date": Date,
                "attendance": Attendance,
                "cans": cans,
                "cooler": cooler,
                "drum": drum,
                "cansPrice": can_price,
                "coolerPrice": cooler_price,
                "drumPrice": drum_price,
                "totalBill": Total_Bill,
                "dues": Dues,
                "paidBill": paid,
            }
        }
        # print(sheet_input)
        daily_sheet_Api(sheet_input=sheet_input)

        # print(self.current_date)


class Upload_monthly_sheet_WT(Upload_Daily_sheet_WT):
    def __init__(self):
        # initialize the parent class
        super().__init__()

    def send_monthly_data(self, date, Monthly_Cans, Monthly_Coolers, Monthly_Drum, Monthly_Bill, Monthly_Paid, Monthly_Dues):

        sheet_input = {
            "monthlySheet": {
                "date": date,
                "monthlyCans": Monthly_Cans,
                "monthlyCoolers": Monthly_Coolers,
                "monthlyDrum": Monthly_Drum,
                "monthlyBill": Monthly_Bill,
                "monthlyPaid": Monthly_Paid,
                "monthlyDues": Monthly_Dues,
            }}

        monthly_sheet_Api(sheet_input=sheet_input)


class Upload_yearly_sheet_WT(Upload_monthly_sheet_WT):
    def __init__(self):
        # initialize the parent class
        super().__init__()

    def send_yearly_data(self, date, yearly_Cans, yearly_Coolers, yearly_Drum, yearly_Bill, yearly_Paid, yearly_Dues):

        sheet_input = {
            "entireHistorySheet": {
                "date": date,
                "yearlyCans": yearly_Cans,
                "yearlyCoolers": yearly_Coolers,
                "yearlyDrums": yearly_Drum,
                "yearlyBill": yearly_Bill,
                "yearlyPaid": yearly_Paid,
                "yearlyDues": yearly_Dues
            }}
       

        yearly_sheet_Api(sheet_input=sheet_input)


if __name__ == "__main__":
    # screen1=Upload_Daily_sheet_WT()
    # screen1.send_daily_data()
    screen2 = Upload_monthly_sheet_WT()
    screen2.send_monthly_data()
