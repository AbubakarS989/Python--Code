from prettytable import PrettyTable

# Create a PrettyTable instance
table = PrettyTable()

# Define the table columns
table.field_names = ["Name", "Age", "City"]

# Function to add rows to the table
def add_person():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    city = input("Enter city: ")

    table.add_row([name, age, city])
    print(f"{name} added to the table.")

# Function to search for a person by name
def search_person():
    name_to_search = input("Enter the name to search: ")
    found_persons = [row for row in table if name_to_search in row.get_string()]
    if found_persons:
        print("\nFound person(s):")
        print(found_persons)
    else:
        print(f"\nNo person found with the name '{name_to_search}'.")

# Function to sort the table by age
def sort_by_age():
    sort_order = input("Enter 'asc' for ascending or 'desc' for descending order: ").lower()
    if sort_order == 'asc':
        table.sortby = "Age"
    elif sort_order == 'desc':
        table.sortby = "Age"
        table.reversesort = True
    else:
        print("Invalid input. Sorting aborted.")

# Ask the user for input and add rows to the table
while True:
    print("\nOptions:")
    print("1. Add person")
    print("2. Search person")
    print("3. Sort by age")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_person()
    elif choice == '2':
        search_person()
    elif choice == '3':
        sort_by_age()
    elif choice == '4':
        print("\nFinal Table:")
        print(table)
        break
    else:
        print("Invalid choice. Please try again.")
