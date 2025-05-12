from user import User


class AccessControl:
    _instance = None

    def __init__(self):
        self._registered_users = {
            1: True,
            2: True,
            3: False
        }
        self._permissions = {
            1: [1, 2],
            2: [1],
        }

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def is_registered(self, user_id: int) -> bool:
        return self._registered_users.get(user_id, False)

    def has_access(self, user_id: int, book_id: int) -> bool:
        return book_id in self._permissions.get(user_id, [])


ACCESS_CONTROL = AccessControl.get_instance()
