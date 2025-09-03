#Interface segration principle tells to seggregate the interface methods in such a way that subclass can implement or can have only the method of the parent class which is relevant to them

#It solves the drawback or problem that might violate Liskov substitute principle

from abc import ABC, abstractmethod

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Wingable(ABC):
    @abstractmethod
    def wing(self):
        pass

class Sparrow(Flyable):    #Sparrow class haing method of interface flyable
    def fly(self):
        print("Sparrow can fly")

class Ostrich(Wingable):  #OStrich class having methods from Wingable interface
    def wing(self):
        print('Ostriches have wings')

def main():
    obj1=Sparrow()

    obj2=Ostrich()

    obj1.fly()

    obj2.wing()

if __name__=="__main__":
    main()