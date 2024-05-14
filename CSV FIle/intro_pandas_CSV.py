# For Data Analysis 
# CSV
# Pandas


# with open("CSV FIle\Weather-Data.csv","r") as f:
#     # readlines convert simple data into list 
#     data=f.readlines()
#     print(data)



# CSV stands for Coma Separated Values 
# import csv library 
import csv
import pandas


# START convert list from cvs file into integer
# with open("CSV FIle\Weather-Data.csv","r") as data_file:
#     # reader convert each row into a separate list
#     data=csv.reader(data_file)
#     temperature=[]
#     # walk thorough  each row 
#     for row in data:
#         # check each row 1 index and remove "tem" and store other values in temperature list
#         if row[1]!="tem":
#             temperature.append(int(row[1]))

#     print(temperature)  
# END convert list from cvs file into integer
    


    # # back to the ccs formate 
    # for i in data:
    #     print(i.strip())



# Read CSV file using pandas module
# Pandas convert csv file into table formate using (csv readers)
data=pandas.read_csv("CSV FIle\Weather-Data.csv")
print(data)
print()
# print particular colum 

#1: print(data["tem"][0])
for data in data["tem"]:
     print(data) 