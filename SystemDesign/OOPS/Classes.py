#Classes, constructors and objects

class Employee:
    
    def __init__(self, name, age):
        self.name=name
        self.age=age
    

    def about(self):
        return 'my name is',self.name,' and my age is', self.age
    


obj=Employee('Karan',21)

print(obj.about())