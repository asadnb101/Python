# Single Level Inheritance

#Base Class
class Person():
    def __init__(self):
        self.name = ''
        self.age = 0
        
    def accept(self):
        self.name = input("Enter Person name: ")
        self.age = int(input("Enter age: "))
        
    def display(self):
        print("Name ", self.name)
        print("Age ",self.age)
 
 # Derived Class       
class Employee(Person):
    def __init__(self):
        self.empid = ""
        self.salary = 0
        self.exp = 0
        
        
    def accept(self):
        super().accept()
        self.empid = input("Enter empid: ")
        self.salary = int(input("Enter salary: "))
        self.exp = input("Enter years of exp: ")
        
    def display(self):
        super().display()
        print("Employee id: ",self.empid)
        print("Salary: ", self.salary)
        print("Experience: ",self.exp)
    
    
class FullTimeEmployee(Employee):
    def __init__(self):
        self.bonus = 0
        
    def accept(self):
        super().accept()
        self.workinghours = input("Enter no of working hours: ")
        
    def calculateBonus(self):
        self.bonus = self.salary * 0.2
        
    def display(self):
        super().display()
        print("Working Hours: ", self.workinghours)
        print("Bonus: ", self.bonus)
        
        
n = FullTimeEmployee()
n.accept()
n.calculateBonus()
n.display()