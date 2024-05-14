import os

def clear_console():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


print(clear_console())


print("HElLO ")