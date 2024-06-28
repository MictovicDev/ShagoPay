from rest_framework import serializers,response,status
from rest_framework.response import Response
from .models import FundWallet

# class CustomDataSerializer(serializers.Serializer):
#     email = serializers.EmailField()
   


class FundWalletSerializer(serializers.Serializer):
    email = serializers.EmailField()
    amount = serializers.IntegerField()
     
    
