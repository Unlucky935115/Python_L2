class Swimmable:
    def swim(self):
        print("This Animal can swim.")

class Walkable:
    def walk(self):
        print("This animal can walk.")

class Crocodile(Swimmable, Walkable):
    def crocodile(self):
        print("This animal is multi talented.")
crocs = Crocodile()
crocs.swim()
crocs.walk()
crocs.crocodile()