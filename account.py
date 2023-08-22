#Create a class account with variables as holder name, acc no ,acc balance
#Two methods as withdraw and deposit.
#User can only withdraw if amount if the acc balcance is more than withdrawal amount

class account():
    def __init__(self, holderName, accountNo, balance):  #constructor parameters
        self.holderName = holderName
        self.accountNo = accountNo
        self.balance = balance
        
        
    def withdrawal(self, amount):
        if self.balance < amount:
            print("Insufficient Balance")
        
        else:
            self.balance = self.balance - amount
            print("Your Balance is ", self.balance)


    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Your account balance: ", self.balance)
        
        
    def display(self):
        print("Name: ", self.holderName)
        print("Account No: ",self.accountNo)
        print("Balance: ", self.balance)
        
n = account("Asad","12345", 20000)
n.display()
n.deposit(2000)
n.withdrawal(12000)