# Generated by Django 5.1.2 on 2024-10-27 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_payments'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='payment_url',
            field=models.URLField(blank=True, max_length=450, null=True, verbose_name='Ссылка на оплату'),
        ),
        migrations.AddField(
            model_name='payments',
            name='session_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ID сессии'),
        ),
    ]
