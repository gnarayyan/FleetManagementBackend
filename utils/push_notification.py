import firebase_admin
from firebase_admin import credentials, messaging
from django.conf import settings


class PushNotification:
    def __init__(self) -> None:
        self.__cred = credentials.Certificate(settings.FCM_CREDENTIAL)
        firebase_admin.initialize_app(self.__cred)

    def send(self, token: str, title: str, body: str, image: str = None) -> bool:
        notification = messaging.Notification(
            title=title, body=body, image=image)
        message = messaging.Message(
            notification=notification, token=token)

        try:
            response = messaging.send(message)
            print("Successfully sent message:", response)
            return True
        except Exception as e:
            print("Error sending message:", e)
            return False

    def sendAtBulk(self, tokens: list[str], title: str, body: str, image: str = None) -> bool:
        notification = messaging.Notification(
            title=title, body=body, image=image)
        message = messaging.MulticastMessage(
            notification=notification, tokens=tokens)

        try:
            response = messaging.send_multicast(message)
            print("Successfully sent messages to",
                  response.success_count, "devices")
            print("Failed on sening messages to",
                  response.failure_count, "devices")
            return True
        except Exception as e:
            print("Error sending messages:", e)
            return False
