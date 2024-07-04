from rest_framework import serializers,response,status
from rest_framework.response import Response
from .models import FundWallet


{"details":{"ref":"CPL-019283","account":"0724731473","settlementBank":"000014","amount":"10","remark":"This is a test"}} 


class PaystackMoneyTransferSerializer(serializers.Serializer):
    transaction_type = serializers.CharField()
    email = serializers.EmailField()
    amount = serializers.IntegerField()


class AirVendMoneyTransferSerializer(serializers.Serializer):
    pass


class ShagoTranferSerializer(serializers.Serializer):
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


     
    
