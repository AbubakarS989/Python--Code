
from prettytable import PrettyTable

# Create a PrettyTable instance

# table = PrettyTable()
# table.field_names = ["Name", "Age", "City"]
# add=print("Enter heading:")
# field=print("Enter fields:")


# table.add_column("Name",["Ali","Ahmad"])
# table.add_column("City",["Sadiqabad","Sadiqabad"])
# table.add_column("Name",["Ali"])
# table.add_column("City",["Sadiqabad"])
# table.add_column("Name",["Ali"])
# table.add_column("City",["Sadiqabad"])
# table.add_column("Name",["Ali"])
# table.add_column("City",["Sadiqabad"])
# print(table)

# Define the table columns
# add=print("Enter field name:")

# # Add rows to the table
# table.add_row(["Alice", 25, "New York"])
# table.add_row(["Bob", 30, "London"])
# table.add_row(["Charlie", 22, "San Francisco"])



# take data from user and store it into table


table = PrettyTable()
table.field_names = ["Name", "Age", "City"]
for _ in range(1):
    name=input("Enter your name:")
    if name=='exit':
        exit()
    else:
        Age=int(input("Enter your age:"))
        City=input("Enter your city:")
        table.add_row([name,Age,City])

# align table to left
table.align="l"
# Print the table
print(table)



num_person=len(table._rows)
print(num_person)
