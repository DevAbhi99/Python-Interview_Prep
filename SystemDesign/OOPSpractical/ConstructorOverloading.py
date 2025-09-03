#Rectangle

from abc import ABC, abstractmethod


#Without constuctor overloading since python allows only one constructor
class Shape(ABC):
    @abstractmethod
    def __init__(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return f'It is rectangle with are {self.length * self.breadth}'
    
class Square(Shape):
    def __init__(self, side):
        self.side=side

    def area(self):
        return f'It is a square with area {self.side}'
    

obj1=Rectangle(1,2)

obj2=Square(2)

print(obj1.area())

print(obj2.area())




#Using constructor overloading

class rectangle:
    def __init__(self, *args):
        if len(args)==1:
            self.length=self.breadth=args[0]
        elif len(args)==2:
            self.length,self.breadth=args
        else:
            raise ValueError('Invalid argument')
        
    def area(self):
        return self.length*self.breadth
    
obj=rectangle(1,2)

print(obj.area())
