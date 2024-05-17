from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quiz APP Using API")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR) 
        self.canvas=Canvas(height=250,width=500,bg="white")
        self.question_text=self.canvas.create_text(150,125,width=300,text="Some question text",fill=THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.score_label=Label(text="Score:",fg="white",bg=THEME_COLOR,font=(20))
        self.score_label.grid(row=0,column=1)

        # button functions
    

        # true_image=PhotoImage(file="images/true.png")
        # false_image=PhotoImage(file="images/false.png")
        self.true_button=Button(text="True",highlightthickness=0,fg="green",font=("Arial",20))
        self.true_button.grid(row=2,column=0)
        self.false_button=Button(text="False",highlightthickness=0,fg="red",font=("Arial",20))
        self.false_button.grid(row=2,column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        q_text=self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text=q_text)