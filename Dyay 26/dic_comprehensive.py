# syntax
#1 list={new_key:new_value for (key,value) in dict.items() }
#2 list={new_key:new_value for (key,value) in dict.items() if items}


# Rough
# list1={key:f"helo{key}" for key in  range(1,100) if key%10==0}
# dict={
#     1:11,
#     2:22,
#     3:33
# }
# list2={key:value for (key,value) in dict.items()  }
# print(list1)
# print(list2)


#Here
import random
# list to dic

# we are loop through each item in list and store as a key
list_name=["ali","ahmad","Usman","Naveed","Ahsan"]

# merge list along random marks and store as key value in the dictionary 
student_score={ student:random.randint(1,100) for student in list_name             }

print(student_score)

# dic to dic

# create new dic of passes student 
# this dict get data from the above dictionary and check one by one score

# if we loop through any dic we will always used items() method to extract key values from the dictionary
     
pass_students={student:score for student,score in student_score.items()  if score>30}

print(pass_students)



# print(len(list_name))
# exercise
count={word:len(word) for word in list_name }
print(count)

# Exercise 1
# split method split each word and store in the list 
sentence="What is the Airspeed Velocity of an Unladen Swallow?"
list_word=sentence.split()
count={word:len(word) for word in list_word }
print(count)

# Exercise 2
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

# weather_f={day:(key*9/5)+32 for (day,key) in weather_c.items()}
# print(weather_f)




# Looping through Pandas Data Frame

student_dic={
    "student":["ali","ahmad","usman","dowaed"],
    "score":[40,56,44,34]
}

import pandas
student_DF= pandas.DataFrame(student_dic)
# print(student_DF)

for (key,value) in student_DF.items():
    print(value)

# Pandas In-build loop
# allows us to loop through each of the rows of  dataFrame  
score=[]
dict_score_name={}
for (index,row) in student_DF.iterrows():
    # print(index)
    # print(row)
    # we can access each row data 
    print(row.score)
    print(row.student)
    score.append(row.score)
    # store data into dic of (dic score name)
    dict_score_name[row.student]=row.score
    # print particular name of data     
    if row.student =="ali":
        print(f"Score of ali is : {row.score}")

print(score)
print(dict_score_name)

