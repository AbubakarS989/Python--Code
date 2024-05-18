#  window 1

#  Selection window
# Which app should the user wanna use

from tkinter import *

# Windows file

from window2 import window_2_simple
from window3 import window_3_quote
from window4 import window_4_auto
from window5 import window_5_end

def window_1_select():
    #  - Welcome Information with key features
    #! --- UI ---
    window=Tk()
    window.title("Email Toolbox App")
    window.config(padx=0,pady=20,bg="lightblue")
    canvas=Canvas(height=600,width=600,bg="lightblue",highlightthickness=0)
    canvas.grid(row=0,column=0)



    #! Label - Welcome Information with key features
    canvas.create_text(290, 40, text="Welcome to Email Toolbox App", font=("Arial", 20,"bold"), fill="black")
    canvas.create_text(280, 70, text="~ Abubakar Hafeez ~", font=("Arial", 16,"bold"), fill="black")
    canvas.create_text(120, 170, text="Select Your Tool:", font=("Arial", 18,"bold"), fill="black")
    canvas.create_text(125, 220, text="1 - Simple Email Sender:", font=("Arial", 14), fill="black")
    canvas.create_text(212, 260, text="2 - On-Click Quote Generated with Email App:", font=("Arial", 14), fill="black")
    canvas.create_text(185, 310, text="3 - On-Click Birthday Wisher Generated\nwith Email App:", font=("Arial", 14), fill="black")

    #! Create Radiobuttons for selecting options
    # Create a variable to hold the selected option
    var = IntVar()
    option1 = Radiobutton(window, text="Option 1", variable=var, value=1)
    canvas.create_window(480, 220, window=option1)

    option2 = Radiobutton(window, text="Option 2", variable=var, value=2)
    canvas.create_window(480, 260, window=option2)

    option3 = Radiobutton(window, text="Option 3", variable=var, value=3)
    canvas.create_window(480, 310, window=option3)

    # Radio BUtton function
    def perform_action():
        selected_option = var.get()
        if selected_option == 1:
            window.destroy()
            window_2_simple()
            window.destroy()
            window_5_end()

        elif selected_option == 2:
            window.destroy()
            window_3_quote()
            window.destroy()
            window_5_end()
        elif selected_option == 3:
            window.destroy()
            window_4_auto()
            window.destroy()
            window_5_end()

    next_button = Button(window, text="  Next  ", bg="grey", fg="white",command=perform_action)
    # Add the button widget to the canvas at position (200, 150)
    canvas.create_window(540, 540,window=next_button)
    window.mainloop()
    



    # window_4_auto() 
    # window_2_simple()
    # window_3_quote()