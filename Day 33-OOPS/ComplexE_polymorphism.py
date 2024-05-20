
# ! polymorphism - one thing is used can be use as different ways
# ! operator overloading
# Operator and Dunder functions
# definition-->
            # when the same operator is allowed to have 
            # different meaning according to context.

# When one operator is used for different work:
# here context is : integer
print(1+2) #3

# here context is : string
print("Hello"+" World") #concatenate two strings

# here context is : list
print([1,2,3]+[4,5,6]) # merge | add two list, return 1 list 

#! --> This is called operator overloading


# Example for Polymorphism 
#TODO Create a class that generate COmplex numbers

# class Complex_Number:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def generate_complex(self):
#         self.real=int(input("Enter number 1:"))
#         self.img=int(input("Enter number 2:"))
        
#         print(f"{self.real}i + {self.img}j")

#     def add_complex(self,number2):
#         # self.real1=int(input("Enter real part of Eq1:"))
#         # self.img1=int(input("Enter imaginary part of Eq1:"))

#         # self.real2=int(input("Enter real part of Eq2:"))
#         # self.img2=int(input("Enter imaginary part of Eq2:"))
#         # self.real=self.real1+self.real2
#         # self.img=self.img1+self.img2
#         # print(f"Equation 1:{self.real1}i+{self.img1}j ")
#         # print(f"Equation 2:{self.real2}i+{self.img2}j ")
#         # print(f"Addition of two complex equations are:{self.real}i +{self.img}j")

#         # Using dunder functions
#         real=self.real+number2.real
#         img=self.img+number2.img
#         return Complex_Number(real,img)


        



# number1=Complex_Number()
# number1.generate_complex()
# number2=Complex_Number()
# number2.generate_complex()

# number3=number1.add_complex(number2)
# number3.generate_complex()




# class Complex_Number:
#     def __init__(self, real=0, img=0):
#         self.real = real
#         self.img = img

#     def generate_complex(self):

#         self.real = int(input("Enter the real part: "))
#         self.img = int(input("Enter the imaginary part: "))
#         sign = '+' if self.img >= 0 else '-'
#         img_part = abs(self.img)  # abs convert it positive 
#         print(f"Complex Number: {self.real}i {sign} {img_part}j")

#     def add_complex(self, number2):
#         real = self.real + number2.real
#         img = self.img + number2.img
#         return Complex_Number(real, img)

#     def display(self):
#         sign = '+' if self.img >= 0 else '-'
#         img_part = abs(self.img)  # abs convert it positive value
#         print(f"{self.real} {sign} {img_part}i")


# # Create first complex number
# number1 = Complex_Number()
# number1.generate_complex()

# # Create second complex number
# number2 = Complex_Number()
# number2.generate_complex()

# # Add the two complex numbers
# number3 = number1.add_complex(number2)

# # Display the result
# number3.display()




#! Operator and Dunder functions -> add 2 underscore start and end of variable

# a__add__b
# a__sub__b 
# a__mul__b
# a__truediv__b
# a__mod__b

 



class Complex_Number:
    def __init__(self, real=0, img=0):
        self.real = real
        self.img = img

    def generate_complex(self):
        self.real = int(input("Enter the real part: "))
        self.img = int(input("Enter the imaginary part: "))
        self.display()

    def __add__(self, number2):
        real = self.real + number2.real
        img = self.img + number2.img
        return Complex_Number(real, img)
    def __sub__(self, number2):
        real = self.real - number2.real
        img = self.img - number2.img
        return Complex_Number(real, img)

    def display(self):
        sign = '+' if self.img >= 0 else '-'
        img_part = abs(self.img)
        print(f"{self.real} {sign} {img_part}i")


# Create first complex number
number1 = Complex_Number()
number1.generate_complex()

# Create second complex number
number2 = Complex_Number()
number2.generate_complex()

# Add the two complex numbers
number3 = number1 + number2
# Display the result
number3.display()

number4=number1-number2
number4.display()

