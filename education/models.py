from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    course_name = models.CharField(max_length=100, verbose_name='Название')
    course_discription = models.TextField(**NULLABLE, verbose_name='Описание')
    course_image = models.ImageField(**NULLABLE, upload_to='education/image/', verbose_name='превью')

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


    def __str__(self):
        return f'{self.lesson_name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'