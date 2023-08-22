#Create a class account with variables as holder name, acc no ,acc balance
#Two methods as withdraw and deposit.
#User can only withdraw if amount if the acc balcance is more than withdrawal amount

class Account():
    def __init__(self):
        self.holderName = ""
        self.accountNo = ""
        self.balance = 0
        
    def person(self):
        self.holderName = input("Enter Holder Name: ")
        self.accountNo = int(input("Enter Account No: "))
        self.balance = float(input("Enter you account balance: "))
        
    
        
    def deposit(self):
        self.diposit = ''
        self.deposit = int(input("Enter deposite amount"))
        self.depositBalance = self.balance + self.deposit
        print("Your deposit balance is: ", self.depositBalance)
        
        
    def withdraw(self):
        self.withdraw = int(input("Enter your withdrawal amount: "))
        if self.balance < self.withdraw:
            print("Insufficient Balance")
            
        else:
            self.balance = self.balance - self.withdraw
            
    def display(self):
        print("Holder Name: ", self.holderName)
        print("Account Number: ",self.accountNo)
        print("Current Balance: ", self.balance)
        print("Deposit Amount: ", self.balance)
        print("Withdrawal Amount: ",self.withdraw)
        
        
n = Account()
n.person()
n.deposit()
n.withdraw()
n.display()