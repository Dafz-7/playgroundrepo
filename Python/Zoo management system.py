
#* Create a zoo management system --> types of animals and their feeding habits
#* Inheritance --> different categories and calculate their daily food requirements

class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    def calculate_food_requirements(self):
        print("Calculate food requirement...")

#*! 3 derived classes
class Mammal(Animal):
    def __init__(self, name, species, age, weight):
        super().__init__(name, species, age)
        self.weight = weight
    def calculate_food_requirements(self):
        return print(f"Daily food requirement for {self.name} ({self.species}): {self.weight * 0.05} kg")

class Bird(Animal):
    def __init__(self, name, species, age, wing_span):
        super().__init__(name, species, age)
        self.wing_span = wing_span
    def calculate_food_requirements(self):
        return print(f"Daily food requirement for {self.name} ({self.species}): {self.wing_span * 0.02} kg")

class Reptile(Animal):
    def __init__(self, name, species, age, length):
        super().__init__(name, species, age)
        self.length = length
    def calculate_food_requirements(self):
        return print(f"Daily food requirement for {self.name} ({self.species}): {self.length * 0.03} kg")

#*! Object creation
main = Animal("pass", "pass", 0)
obj1 = Mammal("Elephant", "Elephantidae", 0, 5000)
obj2 = Bird("Eagle", "Accipitridae", 0, 2.5)
obj3 = Reptile("Crocodile", "Crocodylidae", 0, 4)

#*! Outputs
main.calculate_food_requirements()
obj1.calculate_food_requirements()
obj2.calculate_food_requirements()
obj3.calculate_food_requirements()
