class User:
    def __init__(self, name: str, is_registered: bool, allowed_books: list[str]):
        self.name = name
        self._is_registered = is_registered
        self.allowed_books = allowed_books

    def is_registered(self) -> bool:
        return self._is_registered

    def has_access(self, book_title: str) -> bool:
        return book_title in self.allowed_books
