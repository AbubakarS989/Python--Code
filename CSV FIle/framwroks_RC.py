import pandas

data=pandas.read_csv("CSV FIle\Weather-Data.csv")
print(type(data))

#--> data frame object
#--> equal to Excel file (2 dimensional RowS and columns )
print()
# print particular colum 

#--> Pandas Series data object
#-->equal to list or colum
#1 print(type(data["tem"]))
for Series in data["temp"]:
     print(Series)

# convert data into dictionary
# convert row and columns into dictionary
data_dic=data.to_dict()
print(data_dic)



# convert series into single list
data_list=data["temp"].to_list()
print(data_list)

# 1:Avg of all temperature
avg_temp=sum(data_list)/len(data_list)
print("\nAvg of all temperatures  is:",avg_temp)

# 2:Avg of all temperature
avg_temp=data["temp"].mean()
print("\nAverage of all temperatures using mean(): \n",avg_temp)

# Find maximum value of temperature series 

print(data["temp"].max())


# Get the data from the desire colum

# both methods works in same way
print(data["day"]) # work like value key pairs (dictionary)
print(data.day)  # work as object (OOPS)

# Get data from the Rows

# data[data["day"]]
# print the desire row using left side value of the desire colum
print(data[data.day=="Monday"])
print(data[data.day=="Tuesday"])


# Find which row of data have highest temperature

max_temperature=data["temp"].max()
print("The max temperature in the given row is:")
print(data[data.temp==max_temperature])


# Get particular day data in row formate

Monday=data[data.day=="Monday"]
print(Monday.condition)


# Convert celsius to fahrenheit
# (0°C × 9/5) + 32 = 32°F
Monday=data[data.day=="Monday"]
# to get the specific row value 
# print(Monday.temp[0])

fahrenheit=(Monday.temp[0]*9/5)+32
print("Temperature in Fahrenheit is:",fahrenheit)

 





