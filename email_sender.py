import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv


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

if __name__ == "__main__":
    send_email("parepoulo91@gmail.com","Test email","This is the first email send by cousin bot.")