# OCP stands for open closed principle which means if you want to add new feature to a code base extend the coded that is create a new class or
#subclass or file and then integrate it with the original code base without touching the original code base

from abc import ABC, abstractmethod 

class Customer(ABC):
    def __init__(self, price):
        self.price=price

    def total(self, option):  #This is a normal function but what if I want to add a new option which is VIP I ahve to change in this function
        if option=='student':
            return self.price*0.5
        elif option=='regular':
            return self.price*0.8
        else:
            return -1
        
    def totPrice(self):  #So this function will follow OCP method where I am gonna implement total method but using OCP principle and without touching the method
        pass

#Student
class Student(Customer):
    def __init__(self, customer:Customer):
        self.cost=customer

    def totPrice(self):
        return self.cost.price*0.5

class Regular(Customer):
    def __init__(self, customer:Customer):
        self.cost=customer
    
    def totPrice(self):
        return self.cost.price*0.8
    

#Without touching the total function or if else statement I created a sub class following the OCP principle to add new feature called VIP
class VIP(Customer):
    def __init__(self, customer:Customer):
        self.cost=customer

    def totPrice(self):
        return self.cost.price*0.2

        

def main():
    obj1=Customer(500)

    print(obj1.total('student'))

    obj2=Student(obj1)

    obj3=Regular(obj1)

    obj4=VIP(obj1)

    print(obj2.totPrice())

    print(obj3.totPrice())

    print(obj4.totPrice())


if __name__=="__main__":
    main()