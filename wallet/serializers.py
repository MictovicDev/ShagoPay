from rest_framework import serializers,response,status
from rest_framework.response import Response
from .models import FundWallet

# class CustomDataSerializer(serializers.Serializer):
#     email = serializers.EmailField()
   
{
"serviceCode" : "WBV",
"amount" : "100",
"bin": "058",
"bank_account":"0000000000",
"bank_name" : "GT Bank"

}

class FundWalletSerializer(serializers.Serializer):
    transaction_type = serializers.CharField()
    email = serializers.EmailField()
    amount = serializers.IntegerField()


class B2BTranferSerializer(serializers.Serializer):
    serviceCode = serializers.CharField()
    amount = serializers.CharField()
    bin = serializers.CharField()
    bank_account = serializers.CharField()
    bank_name = serializers.CharField()

class VTUSerializer(serializers.Serializer):
    serviceCode = serializers.CharField()
    amount = serializers.CharField()
    phone = serializers.CharField()
    vend_type = serializers.CharField()
    network = serializers.CharField()


     
    
