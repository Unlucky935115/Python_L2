
class A:
    def say_hello(self):
        print("Hello from A")

class B(A):
    def say_hello(self):
        print("Hello from B")

class C(A):
    def say_hello(self):
        print("Hello from C")

class D(B, C):
    def say_hello(self):
        print("Hello from D")

class E(D):
    def say_hello(self):
        print("Hello from E")

print(E.__mro__)
print(type(E.__mro__))
print(E.mro())
print(type(E.mro()))