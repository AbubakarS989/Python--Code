from tkinter import *

# Windows file

from window1 import window_1_select



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
canvas.create_text(214,120,text="Empower your email communications with our suite of tools.",font=("Arial", 11), fill="black")
canvas.create_text(98,140,text="Simple Email Sender:",font=("Arial", 12,"bold"), fill="black")
canvas.create_text(245,159,text="Effortlessly compose and send emails with our easy-to-use interface.",font=("Arial", 11), fill="black")
canvas.create_text(195,178,text="Email Sender with On-Click Generated Quotes:",font=("Arial", 12,"bold"), fill="black")
canvas.create_text(215,205,text="Add a personal touch to your emails with inspirational quotes\nautomatically inserted into your messages.",font=("Arial", 11), fill="black")
canvas.create_text(202,232,text="On-Click Generate Birthday Template Email App:",font=("Arial", 12,"bold"), fill="black")
canvas.create_text(198,260,text="Effortlessly send personalized birthday wishes with our\nauto-generated email templates tailored for birthdays.",font=("Arial", 11), fill="black")
canvas.create_text(72,296,text="Key Features:",font=("Arial", 12,"bold"), fill="black")
canvas.create_text(285,340,text="- Streamlined Workflow: Simplify your email tasks with our user-friendly tools.\n- Personalization: Tailor your emails to make meaningful connections with recipients.\n- Efficiency: Save time and effort with automated features and intuitive design.\n- Enhanced Communication: Elevate your email communications to the next level.",font=("Arial", 11), fill="black")
canvas.create_text(72,530,text="Get Started:",font=("Arial", 16,"bold"), fill="black")
canvas.create_text(213,560,text="Click 'Next' below to explore our suite of email tools and\nrevolutionize your email experience!",font=("Arial", 13), fill="black")


def next_part():
    # window_1_select()
    window.destroy()
    # time.sleep(1)
    window_1_select()
    
# ! BUtton
next_button = Button(window, text="  Next  ", bg="grey", fg="white",command=next_part)
# Add the button widget to the canvas at position (200, 150)
canvas.create_window(540, 540,window=next_button)


window.mainloop()



# window_4_auto() 
# window_2_simple()
# window_3_quote()