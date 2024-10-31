from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from education.models import Course, Lesson, Subscriptions
from education.paginations import CustomPagination
from education.serizlizers import (CourseDetailSerializer, CourseSerializer,
                                   LessonSerializer, SubscriptionsSerializer)
from users.permissions import IsModer, IsOwner
from education.tasks import mail_update_course_info

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    pagination_class = CustomPagination
    serializer_class = CourseSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CourseDetailSerializer
        return CourseSerializer

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def perform_update(self, serializer):
        instance = serializer.save()
        mail_update_course_info.delay(instance.pk)
        return instance

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (IsAuthenticated, ~IsModer,)
        elif self.action in ["update", "partial_update", "retrieve"]:
            self.permission_classes = (IsAuthenticated, IsModer | IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (IsAuthenticated, ~IsModer | IsOwner,)
        return super().get_permissions()






class LessonCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (~IsModer, IsAuthenticated)

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = CustomPagination


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModer | IsOwner)


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModer | IsOwner)


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class SubscriptionsCreateAPIView(generics.CreateAPIView):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsSerializer
    permission_classes = (~IsModer, IsAuthenticated)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_id)
        subs_item = Subscriptions.objects.filter(user=user, course=course_item)
        if subs_item.exists():
            subs_item.delete()
            message = 'подписка удалена'
        else:
            Subscriptions.objects.create(user=user, course=course_item)
            message = 'подписка добавлена'
        return Response({"message": message})


class SubscriptionsListAPIView(generics.ListAPIView):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsSerializer
