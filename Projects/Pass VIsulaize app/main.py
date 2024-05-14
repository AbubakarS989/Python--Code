
# ! import
import pyperclip  # for copy and paste to clip board
import json
import random
from tkinter import messagebox
from tkinter import *
print("Welcome back!")
print("05-07-2024")


# ! file system
# f=open("secret.txt","a")
# f.write()
# f.close()


#! Features
# 1 Auto curser at top left side
# 2 Auto add gmail while open an app
# 3 pop up to tell the use, your pass is saved successfully
# copy to clip board
# generate password
# search the website data through word
#  save data in Json in formatted way

# ! Json Keywords
# json.dump()    --< write
# json.load()    --< read
# json.update()  --< update


#!   Password Generation
def password_generate():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)
    # Generate and print the random numbers
    # list comprehension
    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letter+password_number+password_symbols
    random.shuffle(password_list)

    # join  join the character and create a string
    password = "".join(password_list)
    # display password in the password box using insert
    pass_entry.insert(0, password)
    # copy to clip board
    pyperclip.copy(password)
    print(f"YOur pss is{password}")


# !  UI Setup Done
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)  # padding
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
# canvas.pack()  #pack() pack the things and display on the canvas
# can't use pack in grid system
canvas.grid(row=0, column=1)

#!Labels add Data Entry
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

# ! Entries for data
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(row=2, column=1)
# 0 start from left and END start from right
email_entry.insert(0, "@gamil.com")
pass_entry = Entry(width=40)
pass_entry.grid(row=3, column=1)


# ! Buttons
# Function
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

# format  to store data in json file
    new_data = {website: {
        "email": email,
        "password": password
    }}
    # before save, user re-check the entered data!
    # use dialog box or message box
    # ! validation to check either of filed are empty
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(
            title="Oops", message="please make sure you haven't  left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\n Password: {password}\n Is it okay to save?")
    
        if is_ok:
            # process of saving the data in file 
            try:
                with open("secret.json", "r") as data_file:
                    #! write data to json
                    # Reading old data
                    data = json.load(data_file)
                    # If file is not found     
            except FileNotFoundError:
                with open("secret.json","w") as data_file:
                    json.dump(new_data,data_file,indent=4)
                #  if file exist
            else:
                # update old data with new data
                data.update(new_data)

                # saving the new data in file
                with open("secret.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                    # clear the already data
                    website_entry.delete(0, END)
                    pass_entry.delete(0, END)

def search():
    website=website_entry.get()
    try:
        with open("secret.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="No Data File is found")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email:{email}\nPassword:{password}" )
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title="Error",message=f"No details for \'{website}\' exist." )

# Buttons

generate_pass_button = Button(text="Generate Password", width=34, command=password_generate)
generate_pass_button.grid(row=4, column=1, columnspan=2)
add_button = Button(text="Add", width=34, command=save)
add_button.grid(row=5, column=1, columnspan=2)
search_button=Button(text="Search",command=search)
search_button.grid(row=1,column=2)

window.mainloop()
