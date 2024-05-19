
# program to add names and age in dict:
class Student_data:
    def __init__(self):
        self.D_dict = {}

    def add_student(self):
        for _ in range(1):
            self.name = input("Enter your name:")
            self.age = int(input("Enter your age:"))
            # D_dict.update({self.name:self.age})
            self.D_dict[self.name] = self.age
        print("Students Add Successfully!")
 
    def find_student(self):
        name = input("Enter required Student Name:")
        if name in self.D_dict:
            print(f"Student:{name}\nAge:{self.D_dict[name]}")
        else:
            print("User is not found!")

    def del_student(self):
        name = input("Enter  Student Name to delete:")
        if name in self.D_dict:
            print(f"The {name} with the age {self.D_dict[name]}is deleted from the Database!")
            del self.D_dict[name]
        else:
            print("User is not found!")

    def record(self):
        if self.D_dict:
            print(self.D_dict)
        else:
            print("First enter data then retrieve it! ")


# class_12=S_data()
# Store Data
# class_12.add_student()

# Print the entire data
# class_12.record()


def student_data():
    class_12 = Student_data()
    while True:
        key = int(input(
            "Select one of the below:\n1:Add Student\n2:Find Student\n3:Delete Student\n4:See Records\n"))
        if key == 1:
            class_12.add_student()
        elif key == 2:
            class_12.find_student()
        elif key == 3:
            class_12.del_student()
        elif key == 4:
            class_12.record()
        else:
            print("Invalid Input")
            return False


# student_data()