from abc import ABC, abstractmethod


# Wrong
class MySQLDatabase:
    def connect_to_db(self):
        print("Connected to MySQL")


class App:
    def __init__(self):
        self.db = MySQLDatabase()


# Right

class Database(ABC):
    @abstractmethod
    def connect_to_db(self): pass


class MySQLDatabase(Database):
    def connect_to_db(self):
        print("Connected to MySQL")


class App:
    def __init__(self, db: Database):
        self.db = db

    def connect_to_db(self):
        self.db.connect()
