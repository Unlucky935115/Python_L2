class Animal:
    def make_sound(self):
        print("Bow Bow!!!")

class Cat(Animal):
    def make_sound(self):
        print("Meow Meow!!!")

cat=Cat()
cat.make_sound()