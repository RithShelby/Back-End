# # The word "polymorphism" means "many forms", 
# # and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():

# class Car:
#     def __init__(self,brand,year):
#         self.brand = brand
#         self.year = year
#     def moveSound(self):
#         print("Cars Sound!")

# class Boat:
#     def __init__(self,brand,year):
#         self.brand = brand
#         self.year = year
#     def moveSound(self):
#         print("Boat Sound!")

# class Plane:
#     def __init__(self,brand,year):
#         self.brand = brand
#         self.year = year
#     def moveSound(self):
#         print("Plane Sound!")

# car1 = Car("BMW","2003")
# boat1 = Boat("YASHI","2011")
# plane1 = Plane("AIRWAY","2004")

# for x in (car1,boat1,plane1):
#     x.moveSound()


# Inheritance Class Polymorphism

class Vehicel:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
    def moveSound(self):
        print("WOWO")


class Car(Vehicel):
  pass

class Boat(Vehicel):
  def moveSound(self):
    print("Sail!")

class Plane(Vehicel):
  def moveSound(self):
    print("Fly!")

car1 = Car("Ford", "2022")       #Create a Car object
boat1 = Boat("Ibiza", "2030") #Create a Boat object
plane1 = Plane("Boeing", "2004")     #Create a Plane object

for x in (car1,boat1,plane1):
   print (x.brand)
   print(x.year)
   x.moveSound()