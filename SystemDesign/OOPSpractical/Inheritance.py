#Inheritance 
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r=r

    def area(self):
        print(3.14*(self.r**2))

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        print(self.length*self.breadth)

obj1=Circle(1)

obj2=Rectangle(1,2)

obj1.area()

obj2.area()
