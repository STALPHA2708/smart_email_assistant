import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

def send_summary_email(summary):
    msg = MIMEText(summary)
    msg["Subject"] = "Today’s Tasks with Reasoning"
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = os.getenv("EMAIL_USER")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(msg["From"], os.getenv("EMAIL_PASS"))
        server.sendmail(msg["From"], [msg["To"]], msg.as_string())
