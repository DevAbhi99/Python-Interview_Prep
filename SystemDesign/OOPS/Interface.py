#Interface is used for 50 ti 100% detail hiding. There is no native way of creating Interface in python. But we can mimic interfaces using abstract classes. Unlike Abstract classes Interface can only have abstract methods and the child class has to implement every abstract method in the interface


from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    
    def start(self):
        print('Started')



#Implementation of multiple inheritance using Interface mimicking




class Car(ABC):

    @abstractmethod
    def carStart(self):
        pass

class Scooty(ABC):

    @abstractmethod
    def scootyStart(self):
        pass


class Vehicle(Car, Scooty):

    def carStart(self):
        print('Starts with a key')

    def scootyStart(self):
        print('Starts with a kick')



obj=Vehicle()

obj.carStart()

obj.scootyStart()