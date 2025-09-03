#Composition is a concept in OOPS where a class is used within another class or a class can use the function of other class without inheriting it


class Engine:
    def start(self):
        return 'Engine has started'
    

class Car:
    def __init__(self, brand):
        self.brand=brand
        self.engine=Engine()  #Used the datamember self.engine as object that instantiate class Engine so that start function can be used in car class
        
    def carStart(self):
        print(f'brand is {self.brand} and the cars {self.engine.start()}')

obj=Car('A5')

obj.carStart()