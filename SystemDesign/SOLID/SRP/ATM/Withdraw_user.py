from ATM_user import ATM
from Card_user import Card

class Withdraw:
    def __init__(self, atm:ATM, card:Card):
        self.add=atm
        self.verify=card

    def withdraw(self, amount):
        if self.verify.validation():
            balance=self.add.transactionDetails[self.verify.cardnumber]
            balance-=amount
            self.add.transactionDetails.update({self.verify.cardnumber:balance})
        else:
            return 'Transaction could not be processed!'
        
        