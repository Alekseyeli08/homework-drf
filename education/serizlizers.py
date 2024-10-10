from rest_framework.serializers import ModelSerializer, SerializerMethodField

from education.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    count_lesson = SerializerMethodField()
    lesson = SerializerMethodField()

    def get_lesson(self, course):
        return [lesson.lesson_name for lesson in Lesson.objects.filter(course=course)]

    def get_count_lesson(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ('course_name', 'course_discription', 'count_lesson', 'lesson')


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
