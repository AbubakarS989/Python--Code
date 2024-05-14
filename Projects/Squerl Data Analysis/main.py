import pandas

data=pandas.read_csv("Squerl Data Analysis\Squirrel_Data.csv")
# Get all colors from the main file
len_Gray=len(data[data["Primary Fur Color"]=="Gray"])
len_Red=len(data[data["Primary Fur Color"]=="Cinnamon"])
len_Black=len(data[data["Primary Fur Color"]=="Black"])
# print(len_Gray)
# color_data["Gray"]=len_Gray
# color_data["Red"]=len_Red
# color_data["Black"]=len_Black

# print(color_data)

color_data={
    "Primary Fur Color": ["Gray","Cinnamon","Black"],
    "Count": [len_Gray,len_Red,len_Black]
}
data_color_file=pandas.DataFrame(color_data)
data_color_file.to_csv("Squerl Data Analysis\Color_Data.csv")





