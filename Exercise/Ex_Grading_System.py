student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Insane": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇
for thing in student_scores:
    marks=int(student_scores[thing])
    if marks>=91:
        student_grades[thing]= "Outstanding"
    elif marks>=81 :
        student_grades[thing]= "Exceeds Expectations"
    elif marks>=71:
        student_grades[thing]= "Acceptable"
    
    elif marks<=70:
        student_grades[thing]= "Fail"
    

# 🚨 Don't change the code below 👇
print(student_grades)