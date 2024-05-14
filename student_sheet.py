import csv
from datetime import datetime

# Function to write data to a CSV file with the current date
def append_to_csv(data):
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_day = datetime.now()
    day_name = current_day.strftime("%A") 
    with open('data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow("")
        writer.writerow([day_name])
        # writer.writerow("")
        for key, value in data.items():
            writer.writerow([current_date, key, value])

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
