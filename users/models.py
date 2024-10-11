from django.contrib.auth.models import AbstractUser
from django.db import models

from education.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(**NULLABLE, upload_to='users/avatars/', verbose_name='аватар')
    phone = models.CharField(**NULLABLE, max_length=40, verbose_name='номер телефона')
    country = models.CharField(**NULLABLE, max_length=50, verbose_name='страна')


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    def __str__(self):
        return self.email

class Payments(models.Model):
    method_choices = [
        ('CASH', 'Наличными'),
        ('TRANSFER', 'Перевод на счет'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    payment_date = models.DateTimeField(auto_now=True, verbose_name='дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплаченный урок')
    payment_amount = models.IntegerField( verbose_name='сумма оплаты')
    payment_method = models.CharField(**NULLABLE, max_length=40, choices=method_choices, verbose_name='способ оплаты')
