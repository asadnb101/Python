#Base Class

class Person():
    def __init__(self):
        self.name = ''
        self.age = 0
        
    def acceptPerson(self):
        self.name = input("Enter person name: " )
        self.age = int(input("Enter age: " ))
        
    def displayPerson(self):
        print("Name", self.name)
        print("Age" , self.age)
        

#Derived Class

class Empolyee(Person):
    def __init__(self):
        self.empid = ''
        self.salary = 0
        self.exp = 0
        
    def acceptEmployee(self):
        self.empid = input("Enter Employee Id: " )
        self.salary = input("Enter salary: " )
        self.exp = input("Enter no of experience: " )
                
    def displayEmployee(self):
        print("Employee Id" , self.empid )
        print("Salary" , self.salary )
        print("Experience", self.exp )
        
        
n = Empolyee()
n.acceptPerson()
n.acceptEmployee()
n.displayPerson()
n.displayEmployee()