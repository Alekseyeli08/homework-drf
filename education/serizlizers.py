from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField

from education.models import Course, Lesson, Subscriptions
from education.validators import validate_forbidden_url


class CourseSerializer(ModelSerializer):
    is_sub = SerializerMethodField(read_only=True)

    def get_is_sub(self, course):
        owner = self.context['request'].user
        subscription = Subscriptions.objects.filter(course=course.id, user=owner.id)
        if subscription:
            return True
        return False

    class Meta:
        model = Course
        fields = ('course_name', 'course_discription', 'course_image', 'owner', 'is_sub')


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
    lesson_link = CharField(validators=[validate_forbidden_url])
    class Meta:
        model = Lesson
        fields = '__all__'

class SubscriptionsSerializer(ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = '__all__'