from django.contrib import admin
from users.models import User, Payments


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'email', 'phone', 'country']


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'paid_course', 'paid_lesson', 'payment_amount', 'payment_method']