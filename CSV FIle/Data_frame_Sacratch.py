import pandas
# TODO Create data frame from the scratch


data_dic={"Students":["ALi","Ahmad","Ahsan"],
        "Scores" :[80,76,90]
}

# Using data frame keyword we are able to create table from simple dictionary
data=pandas.DataFrame(data_dic)
print(data)
# Now save data into CSV file
data.to_csv("CSV FIle/New Dic.csv")
 
