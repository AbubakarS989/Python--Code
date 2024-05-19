# Class level methods are called static methods
# Static method that does'nt use any self parameter


class Student:
    @staticmethod  # it is called decorator
    def helo():
        print("HI this is initializing of an object!")


student_1=Student()
student_1.helo()
# it take no argument and no self VAr as well 





