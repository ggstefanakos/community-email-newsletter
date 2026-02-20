import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from email.message import EmailMessage
from email.utils import formataddr


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

if __name__ == "__main__":

    body_html = f"""\
    <html>
      <body>
        <p>This is the <strong>first</strong> email send by cousin bot.</p>
      </body>
    </html>
    """
    send_email_variant("parepoulo91@gmail.com","Test email","This is the first email send by cousin bot.",body_html)

