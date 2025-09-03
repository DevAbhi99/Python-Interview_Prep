#Bank System

class BankAccount:
    account_number:int

    def __init__(self, account_number):
        self.account_number=account_number
        self.balance=0

    hm={}

    def deposit(self,amount):
        self.balance+=amount
        self.hm.update({f'{self.account_number}':f'{self.balance}'})
        print(amount,'is deposited',' the balance is',self.balance)

    def withdraw(self, amount):
        self.balance-=amount
        self.hm.update({f'{self.account_number}':f'{self.balance}'})
        print(amount,'is withdrawn',' the balance is',self.balance)

    def getBalance(self, account_number):
        print(self.hm[f'{account_number}'])
    

obj=BankAccount(123456)

obj.deposit(1000)

obj.withdraw(100)

obj.getBalance(123456)


