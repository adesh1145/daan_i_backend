from django.conf import settings
from django.core.mail import send_mail


def sendEmail(subject: str, message: str, senderEmail: str):
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, [senderEmail])
