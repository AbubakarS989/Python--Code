# Window 3


from window5 import window_5_end

# ! Quote Email App 
import random
from tkinter import *
from tkinter import messagebox
from Email_emplate import Send_Email

# ! features
# Generate Quotes
# the content delete before the new quote display
# email security
# Email Template 
# Make it colorful


def window_3_quote():
#! --- UI ---
    window=Tk()
    window.title(" Quote Email App~ Option 2")
    window.config(padx=0,pady=20,bg="lightblue")
    canvas=Canvas(height=600,width=650,bg="lightblue",highlightthickness=0)
    canvas.grid(row=0,column=0)

    #! Label
    email_text=canvas.create_text(120, 80, text="Receiver Email", font=("Arial", 14), fill="blue")
    subject_text=canvas.create_text(89, 130, text="Subject", font=("Arial", 14), fill="blue")
    body_text=canvas.create_text(97, 190, text="Message", font=("Arial", 14), fill="blue")

    # ! Entry
    email_entry = Entry(window, width=40)
    email_entry.insert(0,"@gmail.com")
    # Add the entry widget to the canvas at position (200, 100)
    canvas.create_window(180, 100, window=email_entry)

    subject_entry=Entry(window,width=40)
    canvas.create_window(180, 150, window=subject_entry)

    message_entry=Text( window,width=55, height=13) 
    canvas.create_window(280, 310, window=message_entry)
    # message=message_entry.get("1.0", "end-1c")


    #! Button Function
    def email_button():
        email=email_entry.get()
        subject=subject_entry.get()
        body=message_entry.get("1.0", "end-1c")
        # print(email)
        # print(subject)
        # print(body)

        # Provide Security to Email
        if len(email)==0 or len(subject)==0 or len(body)==0:
            messagebox.showerror(title="Check Email",message="Please Fill your data!")
        else:
            is_ok=messagebox.askokcancel(title="Check Email",message=f"Are you sure\nto send this Email to {email}?")
            if is_ok:
                # # loading window
                # messagebox.showinfo(title="Loading",message="Message is being send, Please Wait!")
                send=Send_Email(email,body,subject)
                messagebox.showinfo(title="Send",message=f"{send}")
            else:
                messagebox.showinfo(title="Check Email",message="You Email is postpone")

    def quote_generate():
        with open("cleaned_quotes.txt") as quote_file:
            all_quotes=quote_file.readlines()
            quote=random.choice(all_quotes)
        print(quote)
        message_entry.delete(1.0,END)
        message_entry.insert(1.0,quote)
    
    canvas.create_text(170, 540, text="When you done your work Click -> ", font=("Arial", 11,"bold"), fill="black")
    def ok_done():
        window.destroy()
        window_5_end()
    # ! BUtton
    generate_button = Button(window, text="Generate Quote", bg="green", fg="white",command=quote_generate)
    # Add the button widget to the canvas at position (200, 150)
    canvas.create_window(150, 450, window=generate_button)

    send_email_button = Button(window, text="Send Email", bg="red", fg="white",command=email_button)
    # Add the button widget to the canvas at position (200, 150)
    canvas.create_window(350, 450, window=send_email_button)
    next_button = Button(window, text="  Ok Done!  ", bg="grey", fg="white",command=ok_done)
    # Add the button widget to the canvas at position (200, 150)
    canvas.create_window(540, 540,window=next_button)

    window.mainloop()


