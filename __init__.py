"""
Todo: 
1. Log onto email and extract first email !
    -Figure out how to remotely access email
        -IMAPCLIENT !
    -Extract email contents !
    -Print it !
"""
import email
from imapclient import IMAPClient
HOST = "imap.mail.yahoo.com"
USERNAME = "nau_rua1996@yahoo.com"
PASSWORD = ""

with IMAPClient(HOST) as server:
    server.login(USERNAME, PASSWORD)
    server.select_folder("INBOX", readonly=True)

    messages = server.search("UNSEEN")
    for uid, message_data in server.fetch(messages, "RFC822").items():
        email_message = email.message_from_bytes(message_data[b"RFC822"])
        print(uid, email_message.get("From"), email_message.get("Subject"))

