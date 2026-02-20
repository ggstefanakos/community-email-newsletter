import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from email.message import EmailMessage
from email.utils import formataddr
import imghdr
import json

load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(recipient,subject,body):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(body,'plain'))

        with smtplib.SMTP(SMTP_SERVER,SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS,recipient,msg.as_string())

        print("Email sent :)")

    except Exception as e:
        print(f"Error sending mail: {e}")

def send_email_variant(receiver,subject,body,body_html):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Robot Cousin",f"{EMAIL_ADDRESS}"))
    msg["To"] = receiver
    msg["BCC"] = EMAIL_ADDRESS

    msg.set_content(body)

    msg.add_alternative(body_html,subtype="html")

    with smtplib.SMTP(SMTP_SERVER,SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS,receiver,msg.as_string())

def send_mail_w_attachment(receivers,subject,body,image):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Robot Cousin",f"{EMAIL_ADDRESS}"))
    msg["To"] = ', '.join(receivers)
    # msg["BCC"] = EMAIL_ADDRESS # this sends to sender as well
    msg.set_content(body)

    with open(image,'rb') as f:
        file_data = f.read()
        file_name = f.name
        file_type = imghdr.what(file_name)

    msg.add_attachment(file_data,maintype="image",subtype=file_type,filename=file_name)

    with smtplib.SMTP_SSL(SMTP_SERVER,465) as server:
        server.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        server.send_message(msg)
     

if __name__ == "__main__":

    body_html = f"""\
    <html>
      <body>
        <p>This is the <strong>first</strong> email send by cousin bot.</p>
      </body>
    </html>
    """
    with open("contacts.json","r") as f:
        receivers = json.load(f)
    send_mail_w_attachment(receivers,"Test email w pix!","This is the first email send by cousin bot. Check out this cool pic!","example.jpg")