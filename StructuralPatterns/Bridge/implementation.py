from abc import abstractmethod, ABC


class DBConnection(ABC):
    @abstractmethod
    def connect(self) -> str:
        pass


class DBConnectionPostgres(DBConnection):
    def connect(self) -> str:
        pass


class DBConnectionMySQL(DBConnection):
    def connect(self) -> str:
        pass


class DBConnectionMongoDB(DBConnection):
    def connect(self) -> str:
        pass