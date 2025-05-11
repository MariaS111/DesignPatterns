from abc import ABC, abstractmethod


# Interface
class BookInterface(ABC):
    @abstractmethod
    def get_book(self) -> str:
        pass
