# Single Level Inheritance

# Base class
class Person():
    def __init__(self):
        self.name = ''
        self.age = 0

    def acceptPerson(self):
        self.name = input("Enter person name ")
        self.age = int(input("Enter person age "))

    def displayPerson(self):
        print("Name", self.name)
        print("Age", self.age)


# Derived Class
class Employee(Person):
    def __init__(self):
        self.empid = ""
        self.salary = 0
        self.experience = 0

    def acceptEmployee(self):
        self.empid = input("Enter Empid name ")
        self.salary = int(input("Enter salary "))
        self.experience = int(input("Enter years of experience "))

    def displayEmployee(self):
        print("Empid", self.empid)
        print("Salary", self.salary)
        print("Experience", self.experience)


n = Employee()
n.acceptPerson()
n.acceptEmployee()
n.displayPerson()
n.displayEmployee()
