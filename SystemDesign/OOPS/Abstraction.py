#Abstraction is meant for detail hiding. The implementation of the method is hidden

#For abstraction implementation there should be an abstract class where there should be atleast one abstract method. If there are multiple abstract methods then the child class can implement any one abstract method


from abc import ABC, abstractmethod

class Vehicle(ABC):  #Abstract base class
    
    @abstractmethod
    def start(self):    #abstract method with no implementation
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def start(self):
        print('Starts with a key')
    
    def stop(Self):
        print('Stops with a key')


class Scooty(Vehicle):

    def start(self):
        print('Starts with a kick')
    
    def stop(Self):
        print('Stops with a kick')



obj1=Car()

obj2=Scooty()


obj1.start()

obj1.stop()

obj2.start()

obj2.stop()
