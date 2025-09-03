#In this section we are going to learn about Single Responsibility principle where every class takes up one responsibility or perform one function
from ATM_user import ATM
from Card_user import Card
from Deposit_user import Deposit
from Register_user import Register
from Withdraw_user import Withdraw
from Student_user import Student


#Demonstration
def main():
    obj1=ATM()
    obj2=Register('123456', '999', obj1)
    obj3=Card('123456', '999', obj1)
    obj4=Deposit(obj1,obj3)
    obj5=Withdraw(obj1,obj3)
    obj6=Student('78912','998', obj1)
    obj7=Card('78912','998', obj1)
    obj8=Deposit(obj1,obj7)


#Part of single responsibility principle
#User will register
    obj2.register()

    obj3.validation()

    obj4.deposit(1000)

    print(obj1.cardDetailsDisplay(),obj1.transactionDetailsDisplay())


#Part of Open Closed Principle
#Student registration

    obj6.studentRegister()

    obj7.validation()

    obj8.deposit(1000)

    print(obj1.cardDetailsDisplay(),obj1.transactionDetailsDisplay())

#Calling main function

if __name__=="__main__":
    main()





