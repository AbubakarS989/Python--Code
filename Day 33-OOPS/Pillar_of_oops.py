# There are four pillars of OOPS.abs

# ! Abstraction
# ! Encapsulation
# ! Inheritance-> types: single,multi-level,multiple
# ! super method- inherit the parent methods
# ! polymorphism - one thing is used can be use as different ways
# ! poly- many , morph -different

# ! Del Keyword
# ! Private (Like) Attributes and methods

# ! Abstraction 
# Means a thing that is not clear at all. 
# Definition
        # Hiding the implementation details of a class and only showing the essential features to the usr
        # The main code of any class is hide from the user 
        # User don't know the backend of the method(function) or class
        # he just use it and the backend is hide from the user until and unless he himself see the backend
        # overall code is hide from the user 
        # he just call or create object from the class and don't need to see the backend code.


# ! Encapsulation
# definition    
        # Wrapping data and functions into single unit(object)

# ! Del Keyword
# it is used in OOPS to del an object or anything like data

# ! Private (Like) Attributes and methods
# add 2 underscore before variable name that make it private and unaccessible from outside the class

# ! Inheritance
# When one class(child/derived) derived the properties and method of another class(parent/base)

# Example-single inheritance type 
class car:
    def door(self):
        print("There are only 4 doors are allowed!")
    def start(self):
        print("Starting the car..")
    def stop(self):
        print("Stop the car..")

    

class toyotacar(car):
    def color(self,color):
        self.color=color
        print(f"car is {self.color}")


car1=toyotacar()
car2=toyotacar()
 
car1.color("green") # from class toyotacar
car1.start() # from class Car
car1.stop() # from class Car
car1.door() # from class Car

car2.color("red") # from class toyotacar
car2.start() # from class Car
car2.stop() # from class Car
car2.door() # from class Car

#! In this way, we can use functions and method from one class to another class easily and this is called inheritance

# !types:
# ! single
# !multi-level
# !multiple




# ! polymorphism - one thing is used can be use as different ways
# ! operator overloading
# Operator and Dunder functions















