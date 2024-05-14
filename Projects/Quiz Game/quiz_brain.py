class brain():
    def __init__(self,list):
        self.qs_number=0
        self.list=list
        self.score=0

    def still_have_qs(self):
        return self.qs_number < len(self.list)
        

    def next_question(self):
        current_Qs=self.list[self.qs_number]
        self.qs_number+=1
        user_input=input(f"Q{self.qs_number}: {current_Qs.text} (True/False): ")
        self.check_ans(user_input,current_Qs.answer)

    def check_ans(self,user_input,answer):
        
        if user_input.lower()==answer.lower():
            print("You got it right !")
            self.score+=1
        else:
            print("That's is wrong")
            print(f"The correct answer is {answer}")

        print(f"You'r current score is :{self.score} out of {self.qs_number}")
        print("\n")


