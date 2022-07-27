from django.core.mail import send_mail
from menu.celery import app

from .service import send
from .models import Contact


@app.task
def send_info_email(user_email):
    send(user_email)