import os
import time
from calculator_art import logo as art
def clear_console():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

# Calculator with list and dic

# Now we create functions according to the operations

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

# dic that contains all functions

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division,
}

clear_console()
new_start = True
while new_start:
    clear_console()
    print(art) 
    num1 = float(input("What's the first number? "))
    should_continue = True
    while should_continue:
        for symbol in operations:
            print(symbol)
        operate = input("Which operation do you want to apply?")
        num2 = float(input("What's the next number? "))
        operations_calculations = operations[operate]
        result = operations_calculations(num1, num2)
        print(f"{num1} {operate} {num2} = {result:.1f}")

        # here we take the next operation and value
        choice = input(
            f"Type 'Y' to continue calculating with {result:.1f}, 'S' to stop the program, or 'N' for a new start: "
        ).lower()
        if choice == "y":
            num1 = result
            should_continue = True
            clear_console()
            print(f"Previous Result: {num1}")
        elif choice == "n":
            num1 = 0
            should_continue = False
        elif choice == "s":
            print("Program Executing.... ")
            time.sleep(2)
            print("Program Executed ")
            should_continue = False
            new_start = False
