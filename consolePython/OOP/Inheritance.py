# # Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# create parent class
class Person:
    def __init__(self,fname,lname):
        self.firstName = fname
        self.lastName = lname
    def printName(self):
        print(self.firstName,self.lastName)        
# create child class
# class Student(Person):
#     pass
# We want to add the __init__() function to the child class (instead of the pass keyword).
# class Student(Person):
#     def __init__(self, fname, lname):
#         Person.__init__(self,fname,lname)

# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationYear = year
# Add Methods
    def welcome(self):
        print("Welcome" , self.firstName , self.lastName , "to the class of" , self.graduationYear)



x = Student("Mike","Yashi",2025)
x.welcome()
# x.printName()
# print(x.graduationYear)