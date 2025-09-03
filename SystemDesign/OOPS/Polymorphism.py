#Polymorphism means many form. So meethods that have same name but have different functions. The concept is called method overloading


from abc import ABC, abstractmethod

class Calculator:

    @abstractmethod
    def calc(self):
        pass



class Sum:

    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def calc(self):
        return self.x+self.y+self.z
    

class Multply:

    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def calc(self):
        return self.x*self.y*self.z
    

class Sub:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    

    def calc(self):
        return self.x-self.y


obj1=Sum(2,3,4)

obj2=Multply(2,3,4)

obj3=Sub(9,1)


print(obj1.calc())

print(obj2.calc())

print(obj3.calc())