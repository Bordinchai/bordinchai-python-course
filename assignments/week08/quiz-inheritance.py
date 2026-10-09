""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def get_info(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nYear:  {self.year}\n"

class Car(Vehicle):
    def __init__(self, brand ,model , year, doors):
        super().__init__(brand, model, year)
        self.doors = doors
    def get_info(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nYear:  {self.year}\nDoors: {self.doors}\n"
    
vehicle = Vehicle("Toyota", "Yaris", "2025")
print(vehicle.get_info())
Toyota = Car("Toyota", "Y", 2100, 4)
print(Toyota.get_info())