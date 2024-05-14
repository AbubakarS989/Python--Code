# Import
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ! message
#  count the number of times a function is called
# ! Password Generate 
count=0
def password_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    nr_letters = random.randint(8,10)
    nr_numbers = random.randint(2,4)
    nr_symbols=random.randint(2,4)

    pass_letters=[random.choice(letters) for _ in range(nr_letters)]
    pass_num=[random.choice(numbers) for _ in range(nr_numbers)]
    pass_symbol=[random.choice(symbols) for _ in range(nr_symbols)]

    Password_list =pass_letters+pass_symbol+pass_num
    random.shuffle(Password_list)

    password="".join(Password_list)

    password_entry.insert(0,password)
    pyperclip.copy(password)
    print(f"Your pas is{password}")
    if(len(password)!=0):
         count+=1
    else:
        count=0
    print(f"{count}")
    
    



#!  UI
# window
window=Tk()
window.title("Pass Mna")
window.config(padx=80,pady=80)
# canvas
canvas=Canvas(height=300,width=250)
image_logo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image_logo)
canvas.grid(row=0,column=1)

# label
website_label=Label(text="Website")
website_label.grid(row=1,column=0)
email_label=Label(text="  Email/Username")
email_label.grid(row=3,column=0)
password_label=Label(text="Password")
password_label.grid(row=5,column=0)

# ! Entries for data
website_entry=Entry(width=50)
website_entry.grid(row=2,column=0,columnspan=2)
email_entry=Entry(width=50)
email_entry.grid(row=4,column=0,columnspan=2)
email_entry.insert(0,"@gmail.com")
password_entry=Entry(width=50)
password_entry.grid(row=6,column=0,columnspan=2)


# Button
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    if(len(website)==0 or len(password)==0 or len(email)==0):
        messagebox.showerror(title="Oops",message="Please Fill your Entries.")
    else:
        messagebox.askokcancel(title="Re-Check",message=f"Are you sure?\n Email: {password}\n Web: {website}\n Pass: {password}")
        with open("pass_demo.txt","a") as file:
            file.write(f"{website} | {email} | {password} \n")
            website_entry.delete(0,END)
            password_entry.delete(0,END)
    

pass_button=Button(text="Generate Pass",width=20,command=password_generate)
pass_button.grid(row=5,column=2)
print(f"{password_generate}")

add_button=Button(text="Add",width=20,command=save)
add_button.grid(row=6,column=2)







window.mainloop()