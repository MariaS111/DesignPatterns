from proxy import BookProxy
from book import BookInterface
from user import User
from auth import AccessControl


def client(book: BookInterface):
    info = book.get_book()
    print(info)


if __name__ == "__main__":
    registered_users = {
        1: True,
        2: True,
        3: False
    }

    permissions = {
        1: [1, 2],
        2: [1],
    }

    access_control = AccessControl(registered_users, permissions)

    user1 = User(1, "Mary")
    user2 = User(2, "Maria")

    book1 = BookProxy(1, access_control, 1)
    client(book1)

    book2 = BookProxy(1, access_control, 2)
    client(book2)

