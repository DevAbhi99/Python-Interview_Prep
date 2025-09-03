#Encapsulation is used for data hiding. The data is not tampered with but the value of the data can be updated and retrieved

class Employee:

    def __init__(self):
        self.salary=0

    
    def setter(self, salary):   #setter method to update the value
        self.salary=salary
    

    def getter(self):       #getter method to retrieve the value
        return self.salary
    


obj=Employee()

obj.setter(20000)

print(obj.getter())
