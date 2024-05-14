# Syntax of Inheritance in Python
# within the class fish , animal is class from where we copy things of animal and add into the Fish class
# Basically we just copy the features of animal class to Fish class
# Next, to use those copied features  we use super().__init__ method to implement things


# class Fish(Animal):
#     def __init__(self):
#         super().__init__()

# Now look at the below example to understand the concept


class Animal_features:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("Inhale Exhale")


# add inherited class name and use super().__init__ we can simply copy all things easily


class Fish(Animal_features):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("I know how to do it!!")
    def breathe(self):
        super().breathe()
        print("Under water ")

whale = Fish()
# we use swim but we not declare swim  Fish class
whale.swim()
# Also we use breathe but we not declare breathe Fish class
whale.breathe()
print(f"The eyes of whale is : {whale.eyes}")


# In this way, we use other class thing and features into other class .
# This method reduce writing code and safe our precious time also
