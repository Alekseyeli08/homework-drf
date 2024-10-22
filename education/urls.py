from django.urls import path
from rest_framework.routers import SimpleRouter

from education.apps import EducationConfig
from education.views import (CourseViewSet, LessonCreateAPIView,
                             LessonDestroyAPIView, LessonListAPIView,
                             LessonRetrieveAPIView, LessonUpdateAPIView,SubscriptionsCreateAPIView, SubscriptionsListAPIView)

app_name = EducationConfig.name


router = SimpleRouter()
router.register('', CourseViewSet)


urlpatterns = [
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-detail'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
    path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('subscriptions/create/', SubscriptionsCreateAPIView.as_view(), name='subscriptions-create'),
    path('subscriptions/', SubscriptionsListAPIView.as_view(), name='subscriptions-list'),
]

urlpatterns += router.urls