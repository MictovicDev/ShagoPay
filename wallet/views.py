from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status,permissions
from rest_framework.response import Response
from .banks import PaymentFactory
import os
from rest_framework import generics
from .serializers import FundWalletSerializer
from .models import Wallet
import json
import requests

# Create your views here.



class FundWalletView(generics.CreateAPIView):
    serializer_class = FundWalletSerializer
    permission_classes = [permissions.AllowAny]
    # queryset = Wallet.objects.all()

    def perform_create(self, serializer):
        url = 'https://api.paystack.co/transaction/initialize'
        headers = {
            "Authorization": f"Bearer {os.getenv('PAYSTACK_SECRET_KEY')}",
            "Content-Type": "application/json"
        }
        if serializer.is_valid():
            json_data = json.dumps(serializer.data)
            response = requests.post(url, headers=headers, data=json_data)

            
        
        
        
    
    # def get(self,request):
