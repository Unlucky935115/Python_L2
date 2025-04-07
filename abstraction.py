from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self,length, breadth):
        self.breadth =breadth
        self.length=length
    
    def area(self):
        return self.breadth*self.length
    
    def perimeter(self):
        return 2*(self.breadth*self.length)

rect= Rectangle(10,20)
print("Area of Rectangle: ",rect.area())
print("Perimeter of Rectangle: ",rect.perimeter())
