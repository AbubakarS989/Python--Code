from tkinter import *

window = Tk()
window.title("Simple Email Sender App")
window.config(padx=80, pady=100)

# Labels
title_label = Label(window, text="Simple Email Sender App", font=("Arial", 30, "bold"), fg="red")
title_label.pack()

receiver_frame = Frame(window)
receiver_frame.pack()

receiver_label = Label(receiver_frame, text="To: ", font=("Arial", 20, "italic"))
receiver_label.pack(side=LEFT)

receiver_entry = Entry(receiver_frame)
receiver_entry.pack(side=LEFT)

subject_label = Label(window, text="Subject: ", font=("Arial", 20, "italic"))
subject_label.pack()

subject_entry = Entry(window)
subject_entry.pack()

message_label = Label(window, text="Message: ", font=("Arial", 20, "italic"))
message_label.pack()

message_entry = Entry(window)
message_entry.pack()

window.mainloop()
