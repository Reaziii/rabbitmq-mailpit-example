from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv


load_dotenv(".env")


class Config(BaseSettings):
    RABBITMQ_USER: str = os.getenv("RABBITMQ_USER")
    RABBITMQ_PASSWORD: str = os.getenv("RABBITMQ_PASSWORD")
    RABBITMQ_HOST: str = os.getenv("RABBITMQ_HOST")
    RABBITMQ_PORT: str = os.getenv("RABBITMQ_PORT")
    SMPT_HOST: str = os.getenv("SMPT_HOST")
    SMPT_PORT: str = os.getenv("SMPT_PORT")
    SMPT_SERVER_ADDRESS: str = os.getenv("SMPT_SERVER_ADDRESS")


config = Config()
