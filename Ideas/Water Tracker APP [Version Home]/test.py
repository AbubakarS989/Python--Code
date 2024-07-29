# import os
# import json

# def ensure_json_file(file_path):
#     """Ensure that the JSON file exists. If not, create it with an empty dictionary."""
#     if not os.path.exists(file_path):
#         print(f"File {file_path} does not exist. Creating a new one.")
#         # Create an empty dictionary or list depending on your needs
#         data = {}
#         with open(file_path, 'w') as file:
#             json.dump(data, file, indent=4)
#         print(f"File {file_path} created successfully.")
#     else:
#         print(f"File {file_path} already exists.")

# # Example usage
# if __name__ == "__main__":
#     file_path = 'data.json'  # Specify your JSON file path here
#     ensure_json_file(file_path)

#     # Now you can proceed with loading and using the JSON file
#     with open(file_path, 'r') as file:
#         data = json.load(file)
#     print("Data loaded from file:", data)


# data=[]
# for _ in range(2):
#     for i in range(1,62):
#         if i >=1 and i<=31:
#             data.append([i,3])
#         elif len(data)>31:
#             data.append([i,4])

# print(data)

# day=data[0][0]
# month=data[0][1]
# print(day)
# print(month)
# for i in range(len(data)):
#     if day and month in data[i]:
#         print("yes")


# MOnthly values
    # Grand Values
        # strip_date=[] 
        # for i in lst_dates:
        #     # print(type(i)) #String
        #     strip_date.append(datetime.strptime(i,"%d-%m-%Y").strftime("%d%m%Y"))
            
        # print(strip_date)
        
        
# Monthly Data
# date_lst = []
        # for date in strip_date:
        #     day = date[0:2]
        #     month = f"{date[2:4]}"
        #     year = f"{date[4:8]}"
        #     date_lst.append([day,month, year])
        # Helper function to parse date strings
            
        # today = datetime.now()  # Today’s date
        # start_of_current_month = today.replace(day=1)  # First day of this month
        # start_of_last_month = (start_of_current_month - timedelta(days=1)).replace(day=1)  # First day of last month
        # end_of_last_month = start_of_current_month - timedelta(days=1)  # Last day of last month
       
        
        # for entry in combine_list.values():
        #     date_str = entry[1][0]['Date']  # Date from the entry
        #     quantity = entry[1][0]  # Quantity is at index 1, and it's the first item in the list
        # entry_date = self.parse_date(date_str)  # Convert date string to date object

        #     if start_of_last_month <= entry_date <= end_of_last_month:
        #         # Add up the values if the date is within the last month
        #         if "Cans" in quantity:    
        #             self.Monthly_Cans += bill_history["Cans"]
        #         if "Cooler":
        #             self.Monthly_Coolers += bill_history["Monthly Cooler"]
        #         if "Drum":
        #             self.Monthly_Drum += bill_history["Drum"]



        # print(date_dict)
import os,json
if not os.path.exists("data.json"):
            with open("data.json", 'w') as f:
                json.dump({}, f)
        
with open("data.json", "r") as f:
    combine_list = json.load(f)
    

billing_info=[]
for entry in combine_list.values():
    # print(entry)
    data=entry[3][0]
    if "Dues" in data:
        billing_info.append(data["Dues"])
        print(billing_info)
        
    # billing_info[]=


print(billing_info)
















