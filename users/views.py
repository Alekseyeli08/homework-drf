from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from users.models import Payments, User

from .serializers import UserSerializer, PaymentSerializer



class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentSerializer
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method',)
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ('payment_date',)

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
