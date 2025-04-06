from abc import ABC, abstractmethod


# Product
class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


# Concrete product
class EmailNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Email is sent: {message}")


# Concrete product
class SMSNotification(Notification):
    def send(self, message: str) -> None:
        print(f"SMS is sent: {message}")


# Concrete product
class TelegramNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Telegram msg is sent: {message}")


# Creator
class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self):
        pass


# Concrete creator
class EmailNotificationFactory(NotificationFactory):
    def create_notification(self) -> EmailNotification:
        return EmailNotification()


# Concrete creator
class SMSNotificationFactory(NotificationFactory):
    def create_notification(self) -> SMSNotification:
        return SMSNotification()


# Concrete creator
class TelegramNotificationFactory(NotificationFactory):
    def create_notification(self) -> TelegramNotification:
        return TelegramNotification()


# Client
def client(creator: NotificationFactory) -> None:
    notifier = creator.create_notification()
    notifier.send(msg_text)


if __name__ == "__main__":
    factories = {
        "email": EmailNotificationFactory(),
        "sms": SMSNotificationFactory(),
        "tg": TelegramNotificationFactory()
    }

    choice = input("Choose notification type (email/sms/tg): ").strip().lower()
    msg_text = input("Enter message: ")

    if choice in factories:
        client(factories[choice])
    else:
        print("Incorrect input")
