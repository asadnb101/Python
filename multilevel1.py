class Person():
    def __init__(self):
        self.name = ''
        self.age = 0
        
    def acceptPerson(self):
        self.name = input("Enter Person name: ")
        self.age = int(input("Enter age: "))
        
    def displayPerson(self):
        print("Name ", self.name)
        print("Age ",self.age)
        
class Employee(Person):
    def __init__(self):
        self.empid = ""
        self.salary = 0
        self.exp = 0
        
        
    def acceptEmployee(self):
        self.empid = input("Enter empid: ")
        self.salary = input("Enter salary: ")
        self.exp = input("Enter years of exp: ")
        
    def displayEmployee(self):
        print("Employee id: ",self.empid)
        print("Salary: ", self.salary)
        print("Experience: ",self.exp)
    
    
class FullTimeEmployee(Employee):
    def __init__(self):
        self.bonus = 0
        
    def acceptFTE(self):
        self.workinghours = input("Enter no of wormking hours: ")
        
    def calculatebonus(self):
        self.bonus = self.salary * 0.2
        
    def displayFTE(self):
        print("Working Hours: ", self.workinghours)
        print("Bonus: ", self.bonus)
        
        
n = FullTimeEmployee()
n.acceptPerson()
n.acceptEmployee()
n.acceptFTE()
n.calculatebonus()

n.displayPerson()
n.displayEmployee()
n.displayFTE()