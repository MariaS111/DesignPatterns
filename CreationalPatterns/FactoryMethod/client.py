from creators import NotificationFactory, EmailNotificationFactory, SMSNotificationFactory, TelegramNotificationFactory


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