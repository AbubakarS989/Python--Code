class Circle:

    def __init__(self,radius=0):
        self.radius=radius
    def area(self):  #3.14r^2
        self.radius=int(input("Enter radius of circle:"))
        self.area_circle=(22/7)*pow(self.radius,2)
        print(f"Area of Circle is:{self.area_circle}")
    def perimeter(self):
        self.radius=int(input("Enter radius of circle:"))
        self.peri=2*(22/7)*self.radius
        print(f"Perimeter of Circle is:{self.peri}")
        




circle1=Circle()
circle1.area()
circle1.perimeter()

