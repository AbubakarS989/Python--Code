
#  Selection window
# Which app should the user wanna use
from tkinter import *

def window_5_end():
    #  - Welcome Information with key features
    #! --- UI ---
    window=Tk()
    window.title("Email Toolbox App")
    window.config(padx=0,pady=20,bg="lightblue")
    canvas=Canvas(height=600,width=600,bg="lightblue",highlightthickness=0)
    canvas.grid(row=0,column=0)



    #! Label - Welcome Information with key features
    canvas.create_text(290, 40, text="Good Bye!", font=("Arial", 20,"bold"), fill="black")
    canvas.create_text(280, 70, text="~ Abubakar Hafeez ~", font=("Arial", 16,"bold"), fill="black")
    canvas.create_text(310, 260, text="Thank You for Using the Email Toolbox!\nWe hope our tools have\nhelped you streamline your email communications\nand made your experience more efficient and enjoyable.\n", font=("Arial", 14,"bold"), fill="black")
   

    # next_button = Button(window, text="  Next  ", bg="grey", fg="white")
    # # Add the button widget to the canvas at position (200, 150)
    # canvas.create_window(540, 540,window=next_button)
    window.mainloop()
    



   
