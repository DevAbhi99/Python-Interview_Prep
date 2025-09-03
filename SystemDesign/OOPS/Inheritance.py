#Inheritance is the concept where the child class can access properties of the parent class

class Parent:

    money=2000000

    def prop(self):
        return 'the property was',self.money




class Child(Parent):

    wealth=30000000000


    def prop(self):
        return super().prop(),'No my wealth is', self.wealth   #This is called method overriding because the implementation of prop method of parent class was changed hence was overriden



obj=Child()


print(obj.prop())