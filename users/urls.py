from django.urls import path
from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig
from users.views import (PaymentsViewSet, UserCreateAPIView, UserDeleteAPIView,
                         UserListAPIView, UserRetrieveAPIView,
                         UserUpdateAPIView)

app_name = UsersConfig.name

router = SimpleRouter()
router.register('payments', PaymentsViewSet)


urlpatterns = [
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('create/', UserCreateAPIView.as_view(), name='user-create'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user-delete'),
    path('', UserListAPIView.as_view(), name='user-list'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user-detail'),
]

urlpatterns += router.urls