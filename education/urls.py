from rest_framework.routers import SimpleRouter
from education.views import CourseViewSet, LessonCreateAPIView, LessonUpdateAPIView, LessonListAPIView, LessonDestroyAPIView, LessonRetrieveAPIView
from education.apps import EducationConfig
from django.urls import path

app_name = EducationConfig.name


router = SimpleRouter()
router.register('', CourseViewSet)


urlpatterns = [
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
    path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson_update')
]

urlpatterns += router.urls