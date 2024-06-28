from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import MyTokenObtainPairSerializer, UserSerializer
from rest_framework import generics
from rest_framework import permissions
from django.dispatch import receiver
from .models import User
from django.db.models.signals import post_save
from wallet.models import Wallet


# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




class CreateUserView(generics.ListCreateAPIView):
     serializer_class = UserSerializer
     permission_classes = [permissions.AllowAny]
     queryset = User.objects.all()

    
@receiver(post_save, sender=User)
def post_save_handler(sender, instance, created, **kwargs):
     if created:
          Wallet.objects.create(owner=instance)
          
