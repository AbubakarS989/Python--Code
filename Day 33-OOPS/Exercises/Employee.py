class employee:
    def __init__(self,role,dep,salary):
        self.role=role
        self.dep=dep
        self.salary=salary
    def showDetails(self):
        print(f"Role: {self.role}")
        print(f"Department: {self.dep}")
        print(f"Salary: {self.salary}")
            


class Engineer(employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Teacher","English",3400)
    def details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

emp1=Engineer("Ahmad",34)
emp1.details
()
emp1.showDetails()
