# Single Level Inheritance

# Base class
class Person():
    def __init__(self):
        self.name = ""
        self.age = 0

    def accept(self):
        self.name = input("Enter person name ")
        self.age = int(input("Enter person age "))

    def display(self):
        print("Name", self.name)
        print("Age", self.age)


# Derived Class
class Employee(Person):
    def __init__(self):
        self.empid = ""
        self.salary = 0
        self.experience = 0
        self.workingHours = 0

    def accept(self):
        super().accept()
        self.empid = input("Enter Empid  ")
        self.salary = int(input("Enter salary "))
        self.experience = int(input("Enter years of experience "))

    def display(self):
        super().display()
        print("Empid", self.empid)
        print("Salary", self.salary)
        print("Experience", self.experience)


class FullTimeEmployee(Employee):
    def __init__(self):
        self.bonus = 0

    def accept(self):
        super().accept()
        self.workingHours = input("Enter working hours ")

    def calculateBonus(self):
        self.bonus = self.salary * 0.2

    def display(self):
        super().display()
        print("Working Hours", self.workingHours)
        print("Bonus", self.bonus)


n = FullTimeEmployee()
n.accept()
n.calculateBonus()
n.display()
