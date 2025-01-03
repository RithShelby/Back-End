# # Use the __init__() function to assign values to object properties, 
# # or other operations that are necessary to do when the object is being created:
# class Person:
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age

# p1 = Person("JoJo", 22)
# p2 = Person("Koko",20)
# print(p1.name)
# print(p1.age)


# # The __str__() function controls what should be returned when the class object is represented as a string.
# # If the __str__() function is not set, the string representation of the object is returned
# class Person:
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} {self.age}"   
# p1 = Person("JoJo", 22)
# p2 = Person("Koko",20)
# print(p1)

# object method 
# class Person:
#     def __init__(self,name , age):
#         self.name = name
#         self.age = age
#     def myFun(self):
#         print("Hello my name is " + self.name , self.age)
# p1 = Person("John",25)
# p1.myFun()

# # self parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

# class Person:
#     def __init__(myCuteObj, name, age):
#         myCuteObj.name = name
#         myCuteObj.age = age

#     def myFunc(e):
#         print("Hello, my name is " + e.name + " and I'm " + str(e.age) + " years old.")

# p1 = Person("John", 36)
# p1.myFunc()
