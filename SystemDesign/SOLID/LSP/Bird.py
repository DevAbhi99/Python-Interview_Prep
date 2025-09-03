# LSP stands for Liskov Substitute Principle which states that if Given subclass and the paren class then the object of the parent class should be replaceable with subclass's object

#Like how the parent class behaves the child class also must behave in the same way. All the methods of the parent class must be implemented by child class


class Bird:
    def fly(self):
        print('Bird flies')


class Sparrow(Bird):
    def fly(Self):
        print('Sparrow flies low')


#But if we add another subclass or child class called Ostrich which doesnt fly and raise an exception then it doesnt behave like parent class Bird so it violates Liskov Substitutes principle

class Ostrich(Bird):
    def fly(Self):
        raise Exception('Ostriches dont fly')



obj1=Bird()

obj2=Sparrow()

obj3=Ostrich()

obj1.fly()

obj2.fly()

obj3.fly()


