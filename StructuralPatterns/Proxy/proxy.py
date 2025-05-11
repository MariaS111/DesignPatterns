from book import BookInterface, Book
from auth import AccessControlInterface


class BookProxy(BookInterface):
    def __init__(self, book_id: int, access_control: AccessControlInterface, user_id: int):
        self.book_id = book_id
        self._access_control = access_control
        self._user_id = user_id
        self._book: Book | None = None

    def get_book(self) -> str:
        if not self._check_access():
            return "Access denied!"
        if self._book is None:
            self._book = Book.load_from_db(self.book_id)
        return self._book.get_book()

    def _check_access(self) -> bool:
        print(f"Checking access for user {self._user_id} to book {self.book_id}")
        if not self._access_control.is_registered(self._user_id):
            print("User is not registered")
            return False
        if not self._access_control.has_access(self._user_id, self.book_id):
            print("Permission denied")
            return False
        return True
