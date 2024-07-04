from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework import status,permissions
from rest_framework.response import Response
import os
from rest_framework import generics
from .serializers import *
from .models import Wallet
import json
import requests
import random
import uuid
from .providers.provider_factory import ProviderFactory



class FundWalletView(generics.CreateAPIView):
    serializer_class = PaystackMoneyTransferSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Wallet.objects.all()
    

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            amount = serializer.data['amount']
            transaction_type = serializer.data['transaction_type']
            payload = json.dumps(serializer.data)
            provider = ProviderFactory.createprovider(transaction_type)
            headers= provider.get_headers()
            response = provider.money_transfer(headers,payload)
        if response.status_code == 200:
            auth_url = response.json()['data'].get('authorization_url')
            reference = response.json()['data'].get('reference')
            wallet = Wallet.objects.get(owner=request.user)
            wallet.balance += amount
            wallet.save()
            return redirect(auth_url)
    

class ShagoMoneyTransferView(generics.CreateAPIView):
    serializer_class = ShagoTranferSerializer
    transaction_type = 'shago'
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            json_data = json.dumps(serializer.data)
            provider = ProviderFactory.createprovider(self.transaction_type)
            headers = provider.get_headers()
            response = provider.money_transfer(headers,payload=json_data)
            return Response(response.json(), status=response.status_code)


class ShagoAirtimeView(generics.CreateAPIView):
    serializer_class = VTUSerializer
    transaction_type = 'shago'
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            json_data = json.dumps(serializer.data)
            provider = ProviderFactory.createprovider(self.transaction_type)
            headers = provider.get_headers()
            response = provider.buy_airtime(headers=headers, payload=json_data)
            return Response(response.json(), status=response.status_code)



            
        
    
