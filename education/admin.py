from django.contrib import admin
from education.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['pk', 'course_name', 'course_discription']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['pk', 'lesson_name', 'lesson_discription', 'lesson_link', 'course']
