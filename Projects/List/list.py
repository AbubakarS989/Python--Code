# create list
# list_name=[["ali",21],["ahmad",34]]
# access of list
# print(list_name[0][0])

# concatenate list of student and class is: 
# list_student = ["ahmad", "ali", "ahsan", "Naveed", "Tayyab"]
# list_class = [11, 12, 11, 11, 12, 12]

# nested_list = []
# for i in range(len(list_student)):
#     nested_list.append([list_student[i],list_class[i]])

# print(nested_list)


#! program to take data and store into list and convert them into nested
import pandas
list_name=[]
list_class=[]
for _ in range(1,2):
    list_name.append(input("Enter name:"))
    list_class.append(input("Enter Class:"))

    
dict_student = {}
for i in range(len(list_name)):
    dict_student[list_name[i]] =  list_class[i]

print(dict_student)
data=pandas.DataFrame(dict_student.items(),columns=["Name","Class"])
data.to_csv("student_data.csv",index=False)


name="ali"
age=20
clas=12
roll=28

dict_data={}

dict_data[name]=[clas,age,roll]
print(dict_data)






