from pydantic import BaseModel


class EmailNotificationModel(BaseModel):
    email: str
    subject: str
    body: str
