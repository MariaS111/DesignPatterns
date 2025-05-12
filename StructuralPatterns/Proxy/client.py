from proxy import BookProxy
from book import BookInterface
from user import User
from auth import AccessControl


def client(book: BookInterface):
    info = book.get_book()
    print(info)


if __name__ == "__main__":

    user1 = User(1, "Mary")
    user2 = User(3, "Maria")

    book1 = BookProxy(1, 1)
    client(book1)

    book2 = BookProxy(1, 3)
    client(book2)

