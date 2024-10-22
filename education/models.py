from django.db import models
from config import settings

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    course_name = models.CharField(max_length=100, verbose_name='Название')
    course_discription = models.TextField(**NULLABLE, verbose_name='Описание')
    course_image = models.ImageField(**NULLABLE, upload_to='education/image/', verbose_name='превью')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, **NULLABLE, on_delete=models.SET_NULL, verbose_name='владелец')

    def __str__(self):
        return f'{self.course_name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=100, verbose_name='Название')
    lesson_discription = models.TextField(**NULLABLE, verbose_name='Описание')
    lesson_image = models.ImageField(**NULLABLE, upload_to='education/image/', verbose_name='превью')
    lesson_link = models.CharField(**NULLABLE, max_length=250, verbose_name='ссылка на видео')
    course = models.ForeignKey(Course, **NULLABLE, on_delete=models.CASCADE, verbose_name='курс')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, **NULLABLE, on_delete=models.SET_NULL, verbose_name='владелец')

    def __str__(self):
        return f'{self.lesson_name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Subscriptions(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, **NULLABLE, on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    course = models.ForeignKey(Course, **NULLABLE, on_delete=models.CASCADE, verbose_name='курс')
    is_sub = models.BooleanField(verbose_name="подписка", default=False)

    def __str__(self):
        return f'{self.user} - {self.course}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'