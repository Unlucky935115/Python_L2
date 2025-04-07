class Animal:
    def sound(self):
        print("Some animal sound.")

class Cat(Animal):
    def sound(self):
        print("Meow Meow!!!")

class Dog(Animal):
    def sound(self):
        print("Bow Bow!!!")

animal=Cat()
animal.sound()
animal = Dog()
animal.sound()
