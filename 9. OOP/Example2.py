#Create a class account with attributes balance and account number.Create methods for debit, credit and printing the balance. 

class Account:
    def __init__(self, balance, accn):
        self.balance = 0
        self.accn = accn 

    def debit(self):
        d_amt = int(input("Enter the amount to be debitted: "))
        self.balance = self.balance - d_amt
        print(f'{d_amt} has been successfully debitted from your account')
        return "Your current balance is ",self.balance
    
    def credit(self):
        c_amt = int(input("Enter the amount to be creditted:"))
        self.balance = self.balance + c_amt
        print(c_amt , " Has ben creditted to your account")
        return "Your current balance is: ", self.balance
    
    def printbal(self):
        return self.balance
    

user1 = Account(0, 123)
user1.debit()