from abc import abstractmethod, ABC


# Implementation
class DBConnection(ABC):
    @abstractmethod
    def connect(self) -> str:
        pass


# Concrete Implementation
class DBConnectionPostgres(DBConnection):
    def connect(self) -> str:
        return "Connected to PostgreSQL"


# Concrete Implementation
class DBConnectionMySQL(DBConnection):
    def connect(self) -> str:
        return "Connected to MySQL"


# Concrete Implementation
class DBConnectionMongoDB(DBConnection):
    def connect(self) -> str:
        return "Connected to MongoDB"
