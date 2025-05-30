import imaplib
import email
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def fetch_latest_emails():
    today = datetime.now().strftime('%d-%b-%Y')

    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL_USER, EMAIL_PASS)
    mail.select("inbox")

    # Get only emails from today
    status, messages = mail.search(None, f'(SINCE "{today}")')
    ids = messages[0].split()
    email_list = []

    for num in ids[-5:]:
        typ, data = mail.fetch(num, '(RFC822)')
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)
        subject = msg["subject"]
        sender = msg["From"]
        date = msg["Date"]
        body = ""

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body += part.get_payload(decode=True).decode("utf-8", errors="ignore")
        else:
            body = msg.get_payload(decode=True).decode("utf-8", errors="ignore")

        email_list.append((subject, body, sender, msg["Date"]))


    mail.logout()
    return email_list
