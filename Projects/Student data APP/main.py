BACKGROUND_COLOR = "#B1DDC6"


from tkinter import *
from tkinter import messagebox
import pandas

# ! -------------- UI -------------- 
window=Tk()
window.title("Student Data Entry App")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
# canvas
# canvas=Canvas(height=300,width=500)
# canvas.config(bg=BACKGROUND_COLOR)
# canvas.grid(row=0,column=1)

# ! Labels

name_label=Label(text="Enter your name:")
name_label.grid(row=1,column=0,)
class_label=Label(text="Enter your class:")
class_label.grid(row=2,column=0,)
roll_label=Label(text="Enter your Roll NO:")
roll_label.grid(row=3,column=0,)
age_label=Label(text="Enter your Age:")
age_label.grid(row=4,column=0,)


#! -- Entries -- 
name_entry=Entry(width=30)
name_entry.grid(row=1,column=1)
class_entry=Entry(width=30)
class_entry.grid(row=2,column=1)
roll_entry=Entry(width=30)
roll_entry.grid(row=3,column=1)
age_entry=Entry(width=30)
age_entry.grid(row=4,column=1)


# !Button
# button function
def Submit_result():
    student_data_dict={}
    name=name_entry.get()
    clas=class_entry.get()
    roll=roll_entry.get()
    age=age_entry.get()
    # collect them into dict as name are key and their corresponding value are age,roll and class
    student_data_dict[name]=[clas,roll,age]
    data = pandas.DataFrame(student_data_dict.values(), index=student_data_dict.keys(), columns=["Class", "Roll", "Age"])
    data.index.name = "Name"
    data.to_csv("class_data.csv")
    




    


add_button=Button(text="Submit",command=Submit_result)
add_button.grid(row=5,column=1)


window.mainloop()