# PascalCase  => Classes CamelCase  snake_case => for var or others


#  Creating a class
# class user:
#     pass


# user_1=user()    # Assign a class
# user_1.name="abubakar"  # Creating a attribute of class
# user_1.id=9831

# #  Printing the attribute which are created outside the class

# print(user_1.name)
# print(user_1.id)



# creating class with constructor
class User_Info():
    def __init__(self,user_name ,id, age):
        #  attributes of class(class will store in var like self.name)
        self.name=user_name
        self.id=id
        self.age=age
        #  method of class (the class can do with attributes)
    def name1(self):
        print(f"Your Id is {self.id}")
        print(f"Your name is {self.name}")
        print(f"Your age is {self.age}")

for _ in range(1):
    Id=input("Enter your Id: ")
    age=input("Enter your age: ")
    name=input("Enter your name: ")
    user_1=User_Info(Id,name,age) 
    # user_2=User_Info(Id,name,age) 

    

user_1.name1()
# user_2.name1()
    