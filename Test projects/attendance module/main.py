
import json,os
from datetime import datetime
import mysql.connector
from dotenv import load_dotenv
load_dotenv()
from google_sheet import send_data_sheet



class attendance_modules:
    
    def __init__(self):
        
        self.current_date = datetime.now().strftime("%d-%m-%Y")
    
    
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user=os.environ["USER"],
                password=os.environ["PASSWORD"],
                # db="typing",
            )
            print("Connection established successfully ")
        except mysql.connector.Error as e:
                print(e)


        # create curser object that help us to execute SQL commands
        self.my_curser = self.db.cursor()
        
    
         # Read JSON
         
        try:
            with open("attendance module/data.json", "r") as f:
                self.data_json = json.load(f)
                
            with open("attendance module/main_data.json", "r") as f:
                self.main_data_json=json.load(f)
                
        except FileNotFoundError:
            print("Error: data.json file not found.")
            self.data_json = {}
            
    
    # insert data
    def insert_json(self,data):
        with open("attendance module/data.json","w")  as f:
            json.dump(data,f,indent=4)
            
    def insert_main_json(self,data):
        with open("attendance module/main_data.json","w")  as f:
            json.dump(data,f,indent=4)
        
    
    
    
    def main(self):
        
        print("-"*50)
        print(" Welcome to Team attendance Program")
        print("1: Attendance")
        print("2: Enter New Member")        
        print("3: Delete Member")        
        print("4: Exit")        
        print("-"*50)   
        key=input("Enter Your option:")
        try:
            key=int(key)
            if key==1:
                self.attendance()
            elif key==2:
                self.new_member()
            elif key== 3:
                print("Exiting from the program...")
                exit()
        except ValueError as e:
            print("Error occurred",e)
    
    
    def attendance(self):
        data=self.data_json
        data1=self.main_data_json
        # print(data)
        print(data1)
        {
            "1": {
                "date": "",
                "attendance": {
                    "present": "",
                    "absent": ""
                        },
            "Total Members": "",
            "Names of Members":[],
        }
    }
        {"1": [
            {"Name": "",
            "Date": "",
            "attendance": "",
            "time_in": "",
            "time_out": "",
            "D_Join": "",
            "D_Left": "",
            "personal detail":{"Phone Number":302,"Address":"home",},
            "Salary":3500,
            },
            ]
        
    }
        
        print("-"*50)
        for item in self.data_json.values():
            item[0]["Name"]=input("Enter name:")
            # print(item[0]["Name"])

       

    def new_member(self):
        pass
    
    def delete_member(self):
        pass

screen=attendance_modules()
screen.attendance()