import smtplib
import os
from email.message import EmailMessage

def send_email_alert(message):
    email = EmailMessage()
    email.set_content(message)

    email["Subject"] = "⚠ System Alert"
    email["From"] = os.getenv("Sender_mail@example.com")
    email["To"] = os.getenv("Recievers_mail@example.com")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(
            os.getenv("Sender_mail@example.com"),
            os.getenv("EMAIL_APP_PASSWORD")
        )
        server.send_message(email)

