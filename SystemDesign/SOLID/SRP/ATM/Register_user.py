from ATM_user import ATM

#Registration of user
class Register:
    def __init__(self, cardnumber, pin, atm:ATM):
        self.add=atm
        self.cardnumber=cardnumber
        self.pin=pin

    def register(self):
        if self.cardnumber not in self.add.cardDetails:
            self.add.cardDetails.update({self.cardnumber:self.pin})
            self.add.transactionDetails.update({self.cardnumber:0})
            return 'You have registered'
        else:
            return 'You are already registered'