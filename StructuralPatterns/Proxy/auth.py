from user import User
from abc import ABC, abstractmethod


class AccessControlInterface(ABC):
    @abstractmethod
    def is_registered(self, user_id: int) -> bool:
        pass

    @abstractmethod
    def has_access(self, user_id: int, book_id: int) -> bool:
        pass


class AccessControl(AccessControlInterface):
    def __init__(self, registered_users: set[int], permissions: dict[int, list[int]]):
        self.registered_users = registered_users
        self.permissions = permissions

    def is_registered(self, user_id: int) -> bool:
        return self.registered_users.get(user_id, False)

    def has_access(self, user_id: int, book_id: int) -> bool:
        return book_id in self.permissions.get(user_id, [])
