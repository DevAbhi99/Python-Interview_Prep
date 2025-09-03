from ATM_user import ATM

class Card:
    def __init__(self, cardnumber, pin, atm:ATM):
        self.cardnumber=cardnumber
        self.pin=pin
        self.validate=atm

    def validation(self):
        if self.cardnumber in self.validate.cardDetails:
            if self.validate.cardDetails[self.cardnumber]==self.pin:
                return True
            else:
                return False
        else:
            return 'You need to register first'
