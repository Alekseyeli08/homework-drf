from django.core.management import BaseCommand

from education.models import Course, Lesson
from users.models import Payments, User


class Command(BaseCommand):

    def handle(self, *args, **options):
        payments_list = [
            {
                'user': User.objects.get(pk=1),
                'payment_date': '2024-03-01',
                'paid_course': Course.objects.get(pk=2),
                'paid_lesson': Lesson.objects.get(pk=2),
                'payment_amount': '1200',
                'payment_method': 'TRANSFER'},
            {
                'user': User.objects.get(pk=1),
                'payment_date': '2024-03-01',
                'paid_course': Course.objects.get(pk=3),
                'paid_lesson': Lesson.objects.get(pk=3),
                'payment_amount': '800',
                'payment_method': 'CASH'},
            {
                'user': User.objects.get(pk=1),
                'payment_date': '2024-03-01',
                'paid_course': Course.objects.get(pk=2),
                'paid_lesson': Lesson.objects.get(pk=3),
                'payment_amount': '2200',
                'payment_method': 'CASH'},
            {
                'user': User.objects.get(pk=1),
                'payment_date': '2024-03-01',
                'paid_course': Course.objects.get(pk=3),
                'paid_lesson': Lesson.objects.get(pk=2),
                'payment_amount': '1800',
                'payment_method': 'TRANSFER'},
        ]


        payments_for_create = []
        for payments_item in payments_list:
            payments_for_create.append(Payments(**payments_item))
        Payments.objects.bulk_create(payments_for_create)