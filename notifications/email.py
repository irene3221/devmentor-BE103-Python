
class EMailNotification:

    def send_notification(self, user_name: str, message: str):
        print("email sent, user name: {}, message: {}".format(user_name,message))
