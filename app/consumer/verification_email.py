from pika.channel import Channel
from app.utils.constants import Exchanges
from loguru import logger
import json
from app.schemas.email_verifiation import EmailNotificationModel
from app.utils.mail import send_mail


def send_email(ch, method, properties, body):
    try:
        email = EmailNotificationModel.model_validate(json.loads(body))
        send_mail(email)
    except Exception as e:
        logger.error("Email format is not correct")
        print(e)


def start_email_verification_consumer(channel: Channel):
    channel.exchange_declare(
        Exchanges.EMAIL_VERIFICATION_CONSUMER,
        exchange_type="direct"
    )
    queue = channel.queue_declare(
        queue=Exchanges.EMAIL_VERIFICATION_CONSUMER,
        exclusive=True
    )
    queue_name = queue.method.queue
    channel.queue_bind(
        queue=queue_name,
        exchange=Exchanges.EMAIL_VERIFICATION_CONSUMER,
        routing_key=Exchanges.EMAIL_VERIFICATION_CONSUMER
    )
    channel.basic_consume(
        queue=queue_name,
        on_message_callback=send_email,
        auto_ack=True
    )
    logger.info("Waitting for consuming...")
    channel.start_consuming()
