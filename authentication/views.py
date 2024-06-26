from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import MyTokenObtainPairSerializer, UserSerializer
from rest_framework import generics
from rest_framework import permissions
from .models import User


# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




class CreateUserView(generics.ListCreateAPIView):
     serializer_class = UserSerializer
     permission_classes = [permissions.AllowAny]
     queryset = User.objects.all()
