from app.consumer.verification_email import start_email_verification_consumer
import pika
import os


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
    start_email_verification_consumer(channel=channel)
