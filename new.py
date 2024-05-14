import csv
from datetime import datetime

# Function to write data to a CSV file with the current date
def append_to_csv(data):
    current_date = datetime.now()
    day_name = current_date.strftime("%A")  # Get the day name
    with open('data1.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([day_name])  # Write the day name in a new line
        for key, value in data.items():
            writer.writerow(["", key, value])  # Print data below the day name

# Main program loop
while True:
    # Take input from the user
    data_dict = {}
    for key in ['Ahsan', 'Ahmad', 'Moiz']:
        data_dict[key] = input(f"Enter a string for {key}: ")

    # Write the data with the current date to a CSV file
    append_to_csv(data_dict)

    print("Data saved to data.csv")

    # Ask if the user wants to continue
    choice = input("Do you want to continue (yes/no)? ").lower()
    if choice != 'yes':
        break
