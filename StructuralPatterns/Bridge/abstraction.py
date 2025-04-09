from implementation import DBConnection


class Platform:
    def __init__(self, dbconnection: DBConnection) -> None:
        self.dbconnection = dbconnection

    def display(self) -> str:
        pass

class WindowsUI(Platform):
    def display(self) -> str:
        pass

class LinuxUI(Platform):
    def display(self) -> str:
        pass

class MacUI(Platform):
    def display(self) -> str:
        pass