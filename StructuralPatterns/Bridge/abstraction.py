from implementation import DBConnection


# Abstraction
class Platform:
    def __init__(self, dbconnection: DBConnection) -> None:
        self.dbconnection = dbconnection

    def display(self) -> str:
        raise NotImplementedError


# Extended Abstraction
class WindowsUI(Platform):
    def display(self) -> str:
        return f"Windows UI - {self.dbconnection.connect()}"


# Extended Abstraction
class LinuxUI(Platform):
    def display(self) -> str:
        return f"Linux UI - {self.dbconnection.connect()}"


# Extended Abstraction
class MacUI(Platform):
    def display(self) -> str:
        return f"Mac UI - {self.dbconnection.connect()}"
