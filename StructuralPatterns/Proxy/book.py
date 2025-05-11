from book_interface import BookInterface


# Subject
class Book(BookInterface):

    BOOK_DATABASE = {
        1: "Test",
        2: "Design patterns"
    }

    def __init__(self, book_id: int, title: str, content: str):
        self.book_id = book_id
        self.title = title
        self.content = content

    @classmethod
    def load_from_db(cls, book_id: int):
        title = cls.BOOK_DATABASE.get(book_id, "Unknown Book")
        content = f"Content of {title}"
        return cls(book_id, title, content)

    def get_book(self) -> str:
        return f"Book: {self.title}, Content: {self.content}"

