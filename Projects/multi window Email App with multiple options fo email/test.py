import tkinter as tk
from tkinter import messagebox


# Create the main window
window= tk.Tk()
root.title("Option Selection")

# Create a variable to hold the selected option
var = IntVar()

# Create Radiobuttons for selecting options
option1 = tk.Radiobutton(root, text="Option 1", variable=var, value=1)
canvas.create_window(150, 450, window=option1)


option2 = tk.Radiobutton(root, text="Option 2", variable=var, value=2)
canvas.create_window(150, 450, window=option2)

option3 = tk.Radiobutton(root, text="Option 3", variable=var, value=3)
canvas.create_window(150, 450, window=option3)


# Create a button to perform action based on the selected option
action_button = tk.Button(root, text="Perform Action", command=perform_action)
action_button.pack(pady=10)

# Run the application
root.mainloop()
