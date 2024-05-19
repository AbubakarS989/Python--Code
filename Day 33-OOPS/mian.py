# class student():
#     def __init__(self):
#         self.name
#         self.age
#         self.level
#     def detail(self,name,age,level):
#         print(f"Your name is: {self.name}\nYour Class is:{self.level}\nYour age is:{self.level}")


# student_1=student.detail()
# student_1.name("Ali")
# student_1.age(21)
# student_1.level(13)


# student_2=student()
# student_2.name("Ahmad")
# student_2.age(12)
# student_2.level(14)


# class Student:
#     name="Ali"

# # object (instances)
# S1=Student()
# S1.name="ahmad"
# print(S1.name)
# S2=Student()
# print(S2.name)


# # Car
# class Car:
#     color="blue"


# # object is created
# car1=Car()
# print(car1.color)

# # <__main__.Car object at 0x000001B2E3F475C0>

# # now from Car Class create more object(photocopies)
# car2=Car()
# print(car2.color)


# Self,class

# class Age:
#     def __init__(self,s_age,name):
#         self.age=s_age
#         self.name=name
#     def detail(self):
#         print(f"Your name  is: {self.name}")
#         print(f"Your age   is: {self.age}")


# age=int(input("Enter your age:"))
# name=input("Enter your name:")
# student1=Age(age,name)
# print(student1) #type

# student1.detail()


# program to add names and age in dict:
# class S_data:
#     def __init__(self):
#         self.D_dict = {}

#     def add_student(self):
#         for _ in range(1):
#             self.name = input("Enter your name:")
#             self.age = int(input("Enter your age:"))
#             # D_dict.update({self.name:self.age})
#             self.D_dict[self.name] = self.age

#     def find_student(self):
#         name = input("Enter required Student Name:")
#         if name in self.D_dict:
#             print(f"Student:{name}\nAge:{self.D_dict[name]}")
#         else:
#             print("User is not found!")

#     def del_student(self):
#         name = input("Enter  Student Name to delete:")
#         if name in self.D_dict:
#             print(f"The {name} with the age {self.D_dict[name]}is deleted from the Database!")
#             del self.D_dict[name]
#         else:
#             print("User is not found!")

#     def record(self):
#         if self.D_dict:
#             print(self.D_dict)
#         else:
#             print("First enter data then retrieve it! ")


# # class_12=S_data()
# # Store Data
# # class_12.add_student()

# # Print the entire data
# # class_12.record()


# def student_data():
#     class_12 = S_data()
#     while True:
#         key = int(input(
#             "Select one of the below:\n1:Add Student\n2:Find Student\n3:Delete Student\n4:See Records\n"))
#         if key == 1:
#             class_12.add_student()
#         elif key == 2:
#             class_12.find_student()
#         elif key == 3:
#             class_12.del_student()
#         elif key == 4:
#             class_12.record()
#         else:
#             print("Invalid Input")
#             return False


# student_data()


# from student_Data_OOPs import student_data
# from student_Data_OOPs import Student_data



# class_7=Student_data()


# class_7.add_student()








# Scope of D_dict: The D_dict attribute is being defined inside the add_student method. This means it is only available within the add_student method and not accessible from other methods like record. To make D_dict accessible throughout the class, it should be defined within the __init__ method.
# Input within a loop: The loop inside add_student runs twice (for _ in range(1,3)), which means it will prompt the user for input twice. If you intend to ask for more than two students, this number should be changed or made dynamic.
# Method calling: To use the S_data class methods correctly, an instance of the class should be created, and then its methods should be called.
