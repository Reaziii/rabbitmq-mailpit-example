import smtplib
from app.schemas.email_verifiation import EmailNotificationModel
from app.core.config import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from loguru import logger


def send_mail(email: EmailNotificationModel):
    with smtplib.SMTP(
        host=config.SMPT_HOST,
        port=config.SMPT_PORT
    ) as email_server:
        msg = MIMEMultipart()
        msg["From"] = config.SMPT_SERVER_ADDRESS
        msg["To"] = email.email
        file = open("app/templates/verification_email.html", "r")
        msg["subject"] = email.subject
        msg.attach(MIMEText(file.read(), "html"))
        file.close()
        email_server.sendmail(
            from_addr=config.SMPT_SERVER_ADDRESS,
            to_addrs=email.email,
            msg=msg.as_string()
        )
        logger.info(f"A message has been sent to - {email.email}")
