


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

class bugatti(toyotacar):
        def engine(self):
            print("Engine of bugatti should be 980 Hours Power..")




car1=toyotacar()
car2=toyotacar()
car3=bugatti()

# Single - inheritance
# car1 
car1.color("green") # from class toyotacar
car1.start() # from class Car
car1.stop() # from class Car
car1.door() # from class Car

# car2
car2.color("red") # from class toyotacar
car2.start() # from class Car
car2.stop() # from class Car
car2.door() # from class Car 

# Multi-level - inheritance
# car3
car3.engine() # from class bugatti
car3.start() # from class Car
car3.stop() # from class Car
car3.door() # from class Car 
car3.color("blue") # from class toyotacar
# ! In this way, we can access the functions of (car,toyotacar) in bugatti class