from celery.decorators import task
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail,EmailMessage


#!send_review_email_task
@task(name='send_email_reminder')
def send_email_reminder(return_date,user_email):
    email_data = EmailMessage(
        'Return Book',
        f"Plase Return Book Until This Time -- {return_date}",
        settings.EMAIL_HOST_USER,
        [user_email, ],
    )
    return email_data.send(fail_silently=False)