import smtplib
import os
from email.mime.text import MIMEText
import random
import string

def send_email(message):
    sender = "SENDER SMS"
    password = "PASSWORD"
    author = 'AUTHOR SMS'
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "SUBJECT"
        server.sendmail(sender, author, msg.as_string())


        return "The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"


def main():
    message = ('TEXT')


if __name__ == "__main__":
    main()
