

# ! In this way, we can access the functions of (car,toyotacar) in bugatti class
#inherit 2 or multiple class as parent class into child class


# ! here car, toyotacar is parent and bugatti is child, bcz bugatti inherit the data of car and toyotacar at a time.

# Example-multiple inheritance type 
class car: #parent
    def __init__(self,type):
        self.type=type
        print(f"Type of car is {self.type}")
    def door(self):
        print("There are only 4 doors are allowed!")
    def start(self):
        print("Starting the car..")
    def stop(self):
        print("Stop the car..")

class toyotacar(): #parent
    def color(self,color):
        self.color=color
        print(f"car is {self.color}")

class bugatti(toyotacar,car): # child of toyotacar and car 
    def __init__(self,type):
        # ! apply changes on parent variable
        super().__init__(type)

    def engine(self):        
        print("Engine of bugatti should be 980 Hours Power..")




car1=toyotacar()
car2=toyotacar()
car3=bugatti("electric")

# Single - inheritance
# car1 
car1.color("green") # from class toyotacar

# car2
car2.color("red") # from class toyotacar


# Multi-level - inheritance
# car3
car3.engine() # from class bugatti
car3.start() # from class Car
car3.stop() # from class Car
car3.door() # from class Car 
car3.color("blue") # from class toyotacar