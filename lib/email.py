import smtplib
import os

class EmailSender:
    def __init__(self):
        self.sender_email = os.environ.get('MY_EMAIL')
        self.sender_password = os.environ.get("MY_PASSWORD")
    ## Sending Email with Python
    def send_email(self, author, recipient):

        my_email = self.sender_email
        password = self.sender_password

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=recipient,
                msg=f"Subject:You were mentioned\n\n{author} mentioned you in thier post."
            )