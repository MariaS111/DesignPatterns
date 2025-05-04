from book import BookInterface, Book
from user import User


class BookProxy(BookInterface):
    def __init__(self, title: str, user: User):
        self._title = title
        self._user = user
        self._book: Book | None = None

    def read(self) -> None:
        if self._check_access():
            if self._book is None:
                self._book = Book(self._title)
            self._book.read()
        else:
            print("Access denied!!!")

    def _check_access(self) -> bool:
        print("Checking access...")
        return self._user.is_registered() and self._user.has_access(self._title)
