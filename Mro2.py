class A:
    def __init__(self):
        print("A's init")
        super().__init__()

class B(A):
    def __init__(self):
        print("B's init")
        super().__init__()

class C(A):
    def __init__(self):
        print("C's init")
        super().__init__()

class D(B,C):
    def __init__(self):
        print("D's init")
        super().__init__()
print("D's MRO is as below:")
d1=D()
