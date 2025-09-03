class Car:
    brand:str   #Three parameters
    model:str
    year:int

    def __init__(self, brand, model, year):
        self.brand=brand
        self.model=model
        self.year=year

    def display_info(self):
        return self.brand,self.model,self.year
    

obj1=Car('Audi', 'A5', 2000)

obj2=Car('Kia', 'Carens', 2025)

print(obj1.display_info())

print(obj2.display_info())



