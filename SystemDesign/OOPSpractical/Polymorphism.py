from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print('Bark')

class Cat(Animal):
    def sound(self):
        print("meow")


obj1=Dog()

obj2=Cat()

obj1.sound()

obj2.sound()