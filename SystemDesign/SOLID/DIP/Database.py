#Dependency inversion: So according to this principle every Logic should depend upon abstraction and not on concrete classes

#What if tomorrow the database technology has to be switched to PostgreSQL So We need to change the  entire dependecy class so Dependency inversion principle is followed


from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

class MySQLDB(Database):
    def connect(self):
        print('Connected to MYSQL database')

    def disconnect(self):
        print('Disconnected from MYSQL Database')

class PostgreSQLDB(Database):
    def connect(self):
        print('Connected to PostgreSQL database')
    
    def disconnect(self):
        print('Disconnected from Postgresql Database')


#Business logic
class Application:
    def __init__(self, db:Database):
        self.database=db

    def appConnect(self):
        self.database.connect()

    def appDisconnect(self):
        self.database.disconnect()

def main():
    obj1=MySQLDB()

    obj2=PostgreSQLDB()

    obj3=Application(obj2)

    obj3.appConnect()

    obj3.appDisconnect()

if __name__=="__main__":
    main()