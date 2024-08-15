
#* Transport management system --> manages different types of vehicles
#* Implement different types of vehicle and calculate fuel efficiency

#*! Main class
class Vehicle:
    def __init__(self, make, model, year, fuel_consumption):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_consumption = fuel_consumption
    def calculate_efficiency(self):
        print("Calculating efficiency...")

#*! Inheritance processes
class Car(Vehicle):
    def __init__(self, make, model, year, fuel_consumption):
        super().__init__(make, model, year, fuel_consumption)
    def calculate_efficiency(self):
        return print(f"Fuel efficiency of {self.model}: {100 / self.fuel_consumption} km/l")

class Truck(Vehicle):
    def __init__(self, make, model, year, fuel_consumption, load_capacity):
        super().__init__(make, model, year, fuel_consumption)
        self.load_capacity = load_capacity
    def calculate_efficiency(self):
        return print(f"Fuel efficiency of {self.model}: {100 / self.fuel_consumption} km/l")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, fuel_consumption):
        super().__init__(make, model, year, fuel_consumption)
    def calculate_efficiency(self):
        return print(f"Fuel efficiency of {self.model}: {100 / self.fuel_consumption} km/l")
    
#*! Object creation
main = Vehicle("pass", "pass", 0, 0)
obj1 = Car("Toyota", "Camry", 0, 7.5)
obj2 = Truck("Ford", "F-150", 0, 1.5, 0)
obj3 = Motorcycle("Yamaha", "YZF-R3", 0, 3.5)

#*! Outputs
main.calculate_efficiency()
obj1.calculate_efficiency()
obj2.calculate_efficiency()
obj3.calculate_efficiency()
