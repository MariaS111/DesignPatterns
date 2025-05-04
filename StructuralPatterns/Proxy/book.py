from abc import ABC, abstractmethod


# Interface
class BookInterface(ABC):
    @abstractmethod
    def read(self) -> None:
        pass


# Subject
class Book(BookInterface):
    def __init__(self, title: str):
        print(f"Loading book '{title}' from DB...")
        self.title = title

    def read(self) -> None:
        print(f"Book {self.title} is loaded.")
