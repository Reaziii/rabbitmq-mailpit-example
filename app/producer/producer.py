import pika
import os
from app.utils.constants import Exchanges
import json
from app.schemas.email_verifiation import EmailNotificationModel


def start_consuming():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=os.getenv("RABBITMQ_HOST"),
            port=os.getenv("RABBITMQ_PORT"),
            credentials=pika.PlainCredentials(
                username=os.getenv("RABBITMQ_USER"),
                password=os.getenv("RABBITMQ_PASSWORD")
            )
        )
    )
    channel = connection.channel()
    channel.exchange_declare(
        exchange=Exchanges.EMAIL_VERIFICATION_CONSUMER,
        exchange_type="direct"
    )
    channel.basic_publish(
        exchange=Exchanges.EMAIL_VERIFICATION_CONSUMER,
        routing_key=Exchanges.EMAIL_VERIFICATION_CONSUMER,
        body=json.dumps(
            EmailNotificationModel(
                email="welldev@welldev.io",
                body="hello world",
                subject="email verification code"
            ).model_dump()
        ),
        properties=pika.BasicProperties(content_type="application/json")
    )
    connection.close()


if __name__ == "__main__":
    start_consuming()
