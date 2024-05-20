# Class level methods are called static methods


#! @staticmethod  
# ! @classmethod
# ! property
#  ! getter 
#  ! setter
#  
# Static method that does'nt use any self parameter or instance attributes
# can't access and modify  class state  and generally use for utility


class Student:
    @staticmethod  # it is called decorator
    def helo():
        print("HI this is initializing of an object!")



student_1=Student()
student_1.helo()
# it take no argument and no self VAr as well 


# ! @classmethod

class  Person:
    name="unknown"
    # def changeName(self,name):
    #     # want to change the value of Class Attr in case of name(unknown) 
    #     # 1:Person.name=name
    #     self.__class__.name=name
    #     # self.name=name
    #     print(f"New name is: {self.name}")

    # pure method to do same thing within a function
    @classmethod
    def changeName(cls,name):
        cls.name=name
        print(f"New name is: {cls.name}")


# In this way, we can apply changes on class attributes directly from function or method


person1=Person()
print(Person.name)
person1.changeName("ali")
print(Person.name)



# ! property

class Student:
    def __init__(self,phy,math,cmp):
        self.math=math
        self.cmp=cmp
        self.phy=phy
    @property
    def percentage(self):
        return str((self.phy+self.math+self.cmp)/3)+"%"




student1=Student(60,89,45)
print(student1.percentage)


# if we want to change the value of any subject, then simple we change it,
student1.phy=89
print(student1.phy)
print(student1.percentage)









 