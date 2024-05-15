from tkinter import *
from tkinter import messagebox


#! Working
# Take Receiver Email
# Take object(Title or purpose)
# Take Message Content
# Click on Submit and the email is send to the receiver
 





#!  --- UI ---
# Simple Email Sender App by Abubakar Hafeez
window=Tk()
window.title("Simple Email Sender App")
window.config(padx=80,pady=100)
# # canvas
# canvas=Canvas(height=200, width=200)
# canvas.grid(row=0,column=0)

# ! Labels 
title_label=Label(text="Simple Email Sender App",font=("Ariel",30,"bold"),fg="red")
title_label.grid(row=0,column=0)

receiver_label=Label(text="To: ",font=("Arial",20,"italic"))
receiver_label.grid(row=1,column=0)

subject_label=Label(text="Subject: ",font=("Arial",20,"italic"))
subject_label.grid(row=2,column=0)

message_label=Label(text="Message: ",font=("Arial",20,"italic"))
message_label.grid(row=3,column=0)

# ! Entries
receiver_entry=Entry()
receiver_entry.grid(row=1,column=1)
receiver_entry.insert(0, "@gmail.com")
subject_entry=Entry()
subject_entry.grid(row=2,column=1)

message_entry=Text( width=34, height=7) 
message_entry.grid(row=3,column=1)

# ! BUtton

def email(message_body, receiver_email, subject):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    # Email configuration
    sender_email = "mhafeezmabubakar@gmail.com"
    password = "fryhdorkfsknzrdl"

    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    body = message_body
    message.attach(MIMEText(body, "plain"))

    # Connect to Gmail's SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)

    # Send email
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)

    # Close the connection
    server.quit()
    messagebox.showinfo(title="Email Send", message="Email sent successfully.")



#! Button Function:
def send_email():
    # get data entered by the user
    receiver_email=receiver_entry.get()
    subject=subject_entry.get()
    message=message_entry.get("1.0", "end-1c")
    print(receiver_email)
    print(subject)
    print(message)
    is_ok=messagebox.askokcancel(title="Check your email",message=f"Are you sure ?\n Receiver:{receiver_email}\nSubject:{subject}\nMessage:{message}")
    if is_ok:
        email(message,receiver_email,subject)
    else: 
        pass



submit_button=Button(text="Send Email",command=send_email)
submit_button.grid(row=4,column=1)







window.mainloop()