from abc import ABC, abstractmethod
from products import EmailNotification, SMSNotification, TelegramNotification


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

