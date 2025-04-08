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