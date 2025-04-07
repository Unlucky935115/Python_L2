class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Vector(self.x-other.x, self.y-other.y)

    def __mul__(self, scalar):
        return Vector(self.x*scalar, self.y*scalar)

    def __truediv__(self, scalar):
        return Vector(self.x/scalar, self.y/scalar)

    def __mod__(self, scalar):
        return Vector(self.x%scalar, self.y%scalar)

    def __lt__(self, other):
        return (self.x**2+self.y**2) < (other.x**2+other.y**2)

    def __le__(self, other):
        return (self.x ** 2 + self.y ** 2) <= (other.x ** 2 + other.y ** 2)

    def __gt__(self, other):
        return (self.x**2+self.y**2) > (other.x**2+other.y**2)

    def __ge__(self, other):
        return (self.x ** 2 + self.y ** 2) >= (other.x ** 2 + other.y ** 2)

    def __eq__(self, other):
        return self.x==other.x and self.y==other.y

    def __ne__(self, other):
        return not self==other

    def __str__(self):
        return "Vector({},{})".format(self.x, self.y)

    def __repr__(self):
        return "Vector({},{})".format(self.x, self.y)

v1=Vector(3,4)
v2=Vector(1,2)
scalar=2

print("Addition: ",v1+v2)
print("Subtraction: ",v1-v2)
print("Multiplication: ", v1*scalar)
print("Division: ", v1/scalar)
print("Modulus: ",v1%scalar)
print("v1 < v2 : ", v1 < v2)
print("v1 <= v2 : ", v1 <= v2)
print("v1 >= v2 : ", v1 >= v2)
print("v1 > v2 : ", v1 > v2)
print("v1 == v2 : ", v1 == v2)
print("v1 != v2 : ", v1 != v2)
print("String Representation: ",str(v1))
print("Official Representation: ", repr(v1))
