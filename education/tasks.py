from celery import shared_task
from django.core.mail import send_mail
from education.models import Course, Subscriptions
from users.models import User
from django.utils import timezone
from django.conf import settings
from datetime import timedelta

@shared_task
def mail_update_course_info(course_pk):
    course = Course.objects.filter(pk=course_pk).first()
    users = User.objects.all()
    for user in users:
        subscription = Subscriptions.objects.filter(course=course_pk, user=user.pk).first()
        if subscription:
            send_mail(
                subject=f'Обновление курса "{course}"',
                message=f'Курс "{course}", на который вы подписаны, обновлен.',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
            )


@shared_task
def check_last_login():
    users = User.objects.filter(last_login__isnull=False)
    today = timezone.now()
    for user in users:
        if today - user.last_login > timedelta(days=30):
            user.is_active = False
            user.save()
