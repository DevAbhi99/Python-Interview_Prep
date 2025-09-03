#Suppose I am new developer and I want to introduce a new feature called student register where when a student
#registers 100 euro is already there in the bank account
#I have used Open closed principle to add a new feature


from ATM_user import ATM

class Student:
    def __init__(self, cardnumber, pin, atm:ATM):
        self.cardnumber=cardnumber
        self.pin=pin
        self.add=atm

    def studentRegister(self):
        if self.cardnumber not in self.add.cardDetails:
            self.add.cardDetails.update({self.cardnumber:self.pin})
            self.add.transactionDetails.update({self.cardnumber:100})
            return 'You have registered as a student'
        else:
            return 'You have already registered as a student'