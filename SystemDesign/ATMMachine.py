# ATM Machine System Design

class ATM:   # Track all card details and balance details mapped to a card
    def __init__(self):
        self.cardDetails = {}  
        self.balance = {}      

    def cardDetail(self):
        return self.cardDetails
    
    def balanceDetails(self):
        return self.balance


class Register:  
    def __init__(self, atm:ATM, cardNumber, pin):
        self.add = atm      
        self.cardNumber = cardNumber
        self.pin = pin

    def register(self):
        self.add.cardDetails.update({self.cardNumber: self.pin})
        if self.cardNumber not in self.add.balance:
            self.add.balance.update({self.cardNumber: 0})


class Card:  
    def __init__(self, atm:ATM, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.validity = atm    

    def validation(self):
        return self.validity.cardDetails.get(self.cardnumber) == self.pin


class Transaction:   
    def __init__(self, atm:ATM, card: Card):
        self.validation = card
        self.deposits = atm
        self.withdraws = atm

    def deposit(self, amount):
        if not self.validation.validation():
            return "Invalid card/pin"
        current = self.deposits.balance.get(self.validation.cardnumber, 0)
        current += amount
        self.deposits.balance.update({self.validation.cardnumber: current})
        return f"Deposited {amount}. Balance = {current}"

    def withdraw(self, amount):
        if not self.validation.validation():
            return "Invalid card/pin"
        current = self.withdraws.balance.get(self.validation.cardnumber, 0)
        if amount > current:
            return "Insufficient funds"
        current -= amount
        self.withdraws.balance.update({self.validation.cardnumber: current})
        return f"Withdrew {amount}. Balance = {current}"




obj1 = ATM()

obj2 = Register(obj1, '123456', '999')
obj2.register()

print("Cards:", obj1.cardDetail())        
print("Balances:", obj1.balanceDetails()) 

# Transaction
obj3 = Card(obj1, '123456', '999')
obj4 = Transaction(obj1, obj3)

print(obj4.deposit(500))                  
print(obj4.withdraw(120))                 
print("Balances:", obj1.balanceDetails()) 
