BACKGROUND_COLOR = "#B1DDC6"


# Imports
from tkinter import *
import pandas
import random
current_card={}
to_learn={}

# ! Get data from CSV
try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")
# print(to_learn)s
    




# ! Button Function
def flip_card():
    
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_bg,image=card_back_img)

def next_card():    
    global current_card , flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_bg,image=card_front_img)
    flip_timer=window.after(3000,func=flip_card)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()

#! -----------------UI---------------------

window=Tk()
window.title("Flash Card App")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas=Canvas(height=526,width=800)
card_front_img=PhotoImage(file=f"images/card_front.png")
flip_timer=window.after(3000,func=flip_card)
card_back_img=PhotoImage(file="images/card_back.png")
card_bg=canvas.create_image(400,263,image=card_front_img)  #centre
# Customized the text on canvas
card_title=canvas.create_text(400,150,text="",font=("Ariel",20,"italic"))
card_word=canvas.create_text(400,263,text="",font=("Ariel",20,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)


#! -----------------UI--------------------- END


# ! BUttons
cross_image=PhotoImage(file="images/wrong.png")
unknown_button=Button(image=cross_image,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)


check_image=PhotoImage(file="images/right.png")
known_button=Button(image=check_image,highlightthickness=0,command=is_known)
known_button.grid(row=1,column=1)

# ! BUttons ENd



next_card()







window.mainloop()

