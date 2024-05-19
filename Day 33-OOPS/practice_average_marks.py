class Solution:
    def __init__(self):
        self.marks={}

    def get_marks(self):
        for _ in range(1,4):
            subject_name=input("Enter your Subject name:\n")
            mark=int(input(f"Enter your {subject_name} marks:\n"))
            self.marks[subject_name]=mark
        print("Data is stored!")
    def avg(self):
        if not self.marks:  # Check if the dictionary is empty
            print("No marks available to calculate the average.")
            return
        total = sum(self.marks.values())  # Sum all the marks
        average = total / len(self.marks)  # Calculate the average
        print(f"Avg Marks is: {average}")


student1_avg=Solution()
student1_avg.get_marks()
student1_avg.avg()


from student_Data_OOPs import student_data

student_data()