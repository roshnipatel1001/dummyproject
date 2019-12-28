from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from .models import Student


@shared_task
def send_email_task():
    student = Student.objects.all()
    for student_data in student:
        from_email = settings.EMAIL_HOST_USER
        to_email = student_data.email
        send_mail('Celery Task Worked!!!!!!!!',
                  'This is proof the task worked in all users!', from_email, [to_email],
                  fail_silently=False, html_message='This is proof the task worked!')
    return None

