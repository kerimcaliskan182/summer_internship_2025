from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Device
from .serializers import UserSerializer, DeviceSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

