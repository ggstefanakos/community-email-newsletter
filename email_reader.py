import imaplib
import email
import os
from dotenv import load_dotenv
import json

with open("contacts.json",'r') as f:
    contacts = json.load(f)

imap_url = "imap.gmail.com"

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

my_mail = imaplib.IMAP4_SSL(imap_url)
my_mail.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
my_mail.select("Inbox")

key = "FROM"
# value = "@gmail.com" # mail address
for value in contacts:
    print(f"--------------Mails from {value}-------------")
    _, data = my_mail.search(None,key,value)

    mail_id_list = data[0].split()

    msgs = []
    for num in mail_id_list:
        typ,data = my_mail.fetch(num,'(RFC822)')
        msgs.append(data)

    for msg in msgs:
        for response_part in msg:
            if type(response_part) is tuple:
                my_msg = email.message_from_bytes((response_part[1]))
                print("_"*58)
                print("from:",my_msg['from'])
                print("sub:",my_msg['subject'])
                print("body:")
                for part in my_msg.walk():
                    if part.get_content_type() == 'text/plain':
                        print(part.get_payload())
