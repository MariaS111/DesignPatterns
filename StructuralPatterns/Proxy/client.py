from proxy import BookProxy
from book import BookInterface
from user import User


def client(book: BookInterface):
    book.read()


if __name__ == "__main__":
    user1 = User("Mary", True, ["Clean Code", "Test"])
    user2 = User("Maria", False, ["Clean Code"])

    book1 = BookProxy("Clean Code", user1)
    client(book1)

    book2 = BookProxy("Clean Code", user2)
    client(book2)
