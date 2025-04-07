class Car:
    def __init__(self,color,speed,brand, people):
        self.color=color #Public Attribute
        self.speed=speed #Public Attribute
        self._brand = brand #Protected Attribute
        self.__people=people # Private Attribute

    def drive(self):
        print("The {} car is driving at a speed of {} km/hr.".format(self.color, self.speed))

    def brand(self):
        print("The brand of the car is {}".format(self._brand))

    def people_onboard(self):
        print("Number of people inside the car: {}".format(self.__people))

my_car= Car("Red",100, "Toyota","4")
print("Car Color: ", my_car.color) #Accessing Public Attribute
my_car.drive() #Accessing Public Method
print("Car Brand: ", my_car._brand) #Protected attribute can still be accessed but should be avoided
my_car.brand() #Recommended way to access the protected attribute
my_car.people_onboard() #Private Attribute must be accessed through a method
print("Number of people: ", my_car.__people) #Raises an AttributeError Exception

