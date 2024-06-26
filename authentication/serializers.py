from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers,response,status
from django.contrib.auth.password_validation import validate_password
import re
from .models import User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
      token = super().get_token(user)
      token['email'] = user.email
      token['username'] = user.username
      
      return token


class UserSerializer(serializers.ModelSerializer):
     password = serializers.CharField(write_only=True, required=True)
     id = serializers.UUIDField(read_only=True,)
     username = serializers.CharField()
     
     
     class Meta:
        model = User
        fields = ('id','email','password','fullname','role','talentprofile')


     def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
     
     def validate_password(self,attrs):
        if len(attrs) < 8:
          raise serializers.ValidationError("Password is too short.")
        # if not re.search(r"[A-Z]", attrs):
        #     raise serializers.ValidationError("Password Should contain a capital letter.")
        if not re.search(r"[a-z]", attrs):
           raise serializers.ValidationError("Password should contain a lower letter.")
        if not re.search(r"\d", attrs):
           raise serializers.ValidationError("Password should contain a digit.")
        # if not re.search(r"[!@#$%^&*]", attrs):
        #    raise serializers.ValidationError("Password should have a special character.")
        return attrs
     
    
class UserSerializer(serializers.ModelSerializer):
     password = serializers.CharField(write_only=True, required=True)
     id = serializers.UUIDField(read_only=True,)
     username = serializers.CharField()
     
     

     class Meta:
        model = User
        fields = ('id','email','password','username')


     def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
     
     def validate_password(self,attrs):
        if len(attrs) < 8:
          raise serializers.ValidationError("Password is too short.")
        if not re.search(r"[A-Z]", attrs):
            raise serializers.ValidationError("Password Should contain a capital letter.")
        if not re.search(r"[a-z]", attrs):
           raise serializers.ValidationError("Password should contain a lower letter.")
        if not re.search(r"\d", attrs):
           raise serializers.ValidationError("Password should contain a digit.")
        if not re.search(r"[!@#$%^&*]", attrs):
           raise serializers.ValidationError("Password should have a special character.")
        return attrs