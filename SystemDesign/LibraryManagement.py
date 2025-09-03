# Library Management System


class Library:
    def __init__(self):      # Library class keeps tracks of all members and books
        self.members = {}    
        self.books = {}     
    
    def membersDetails(self):
        return self.members
    
    def booksDetails(self):
        return self.books


class Book:
    def __init__(self, bookid, title, author):  # Book class has details about books and if the book is borrowed or not
        self.bookid = bookid
        self.title = title
        self.author = author
        self.isBooked = False 

    def bookDetails(self):
        return [{
            'id': f'{self.bookid}',
            'title': f'{self.title}',
            'author': f'{self.author}',
            'status': f'{"Booked" if self.isBooked else "Available"}'
        }]
        
    def bookChecker(self):
        return self.isBooked


class Member:
    def __init__(self, memberid):  
        self.memberid = memberid
        self.borrow = Library()
        self.returns = Library()
        self.bookDetails = None  
    
    def borrowBook(self, bookid):
        if self.bookDetails is None or self.bookDetails.bookid != bookid:
            return 'No such book attached to this member.'
        
        if self.bookDetails.bookChecker():
            if self.borrow.members.get(bookid) == self.memberid:
                return 'The book was booked by you'
            else:
                return 'The book is not available'
        else:
            self.borrow.members.update({bookid: self.memberid})
            self.borrow.books.update({bookid: True})
            self.bookDetails.isBooked = True
            return 'Book successfully booked'

    def returnBook(self, bookid):
        if self.bookDetails is None or self.bookDetails.bookid != bookid:
            return 'No such book attached to this member.'
        
        if self.bookDetails.bookChecker():
            if self.returns.members.get(bookid) == self.memberid or self.borrow.members.get(bookid) == self.memberid:
                self.returns.books.update({bookid: False})
                if bookid in self.returns.members:
                    self.returns.members.update({bookid: None})
                if bookid in self.borrow.members:
                    self.borrow.members.pop(bookid, None)
                self.bookDetails.isBooked = False
                return 'Book returned'
            else:
                return 'Book is booked but not yours'
        else:
            return 'Book is available in the library'


obj1 = Library()                              
obj2 = Book(1, 'Famous 5', 'Enid Blyton')    
obj3 = Member(101)                            


obj3.bookDetails = obj2


obj3.borrow.books[obj2.bookid] = obj2.isBooked 


print(obj2.bookChecker())         


print(obj3.borrowBook(1))          
print(obj2.bookChecker())          

obj3.returns.members[1] = 101
print(obj3.returnBook(1))        
print(obj2.bookChecker())        
