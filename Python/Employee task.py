# creating an employee management system for a company.
# HOW THE PROGRAM WORKS:
# different types of employees
# calculate their salaries

#class creation
class Employee:
    def __init__(self, name):
        self.name = name
    def calculate_salary():
        print("Calculating salary...")

class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary
    def fullTime(self):
        print(f"Montly salary of {self.name}: ${self.monthly_salary}")

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def partTime(self):
        print(f"Salary of {self.name}: ${(self.hourly_rate) * (self.hours_worked)}")

class ContractEmployee(Employee):
    def __init__(self, name, contract_amount, contract_duration):
        super().__init__(name)
        self.contract_amount = contract_amount
        self.contract_duration = contract_duration
    def contract(self):
        print(f"Monthly salary of {self.name}: ${(self.contract_amount) / (self.contract_duration)}")

#object/instance creation
employee1 = FullTimeEmployee("Alice", 5000)
employee2 = PartTimeEmployee("Bob", 20, 100)
employee3 = ContractEmployee("Charlie", 24000, 6)

#output
employee1.fullTime()
employee2.partTime()
employee3.contract()