class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print("{} is Hunting.".format(self.name))

class Dog(Animal):
    def bark(self):
        print("{} is Running.".format(self.name))

my_dog=Dog("Bruce")
my_dog.eat()
my_dog.bark()