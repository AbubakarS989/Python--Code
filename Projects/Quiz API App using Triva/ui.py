from tkinter import *
import time
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

    

        # true_image=PhotoImage(file="images/true.png")
        # false_image=PhotoImage(file="images/false.png")
        self.true_button=Button(text="True",highlightthickness=0,fg="green",font=("Arial",20),command=self.true_pressed)
        self.true_button.grid(row=2,column=0)
        self.false_button=Button(text="False",highlightthickness=0,fg="red",font=("Arial",20),command=self.false_pressed)
        self.false_button.grid(row=2,column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.config(bg="yellow")
            self.canvas.itemconfig(self.question_text,text="You've reached the end of quiz")
            self.true_button.config(state="disable")
            self.false_button.config(state="disable")
    # button functions
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
        
    def false_pressed(self):    
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)


