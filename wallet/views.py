from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework import status,permissions
from rest_framework.response import Response
from .banks import TransactionFactory
import os
from rest_framework import generics
from .serializers import *
from .models import Wallet
import json
import requests
import random
from .airtime_data import AirtimeDataFactory
# Create your views here.
import uuid


class FundWalletView(generics.CreateAPIView):
    serializer_class = FundWalletSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Wallet.objects.all()
    

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # serializer = FundWalletSerializer(data=request.data)
        url = 'https://api.paystack.co/transaction/initialize'
        paystack_secret = 'sk_test_385e0466b47d91a5b8a16112cdcf34af73c077a7'
        headers = {
            "Authorization": f"Bearer {paystack_secret}",
            "Content-Type": "application/json"
        }
        if serializer.is_valid():
            amount = serializer.data['amount']
            json_data = json.dumps(serializer.data)
            response = requests.post(url, headers=headers, data=json_data)
        if response.status_code == 200:
            auth_url = response.json()['data'].get('authorization_url')
            reference = response.json()['data'].get('reference')
            # FundWalletView.verify_payment(reference)
            wallet = Wallet.objects.get(owner=request.user)
            wallet.balance += amount
            wallet.save()
            return redirect(auth_url)
    

class B2BTransferView(generics.CreateAPIView):
    serializer_class = B2BTranferSerializer
    permission_classes = [permissions.IsAuthenticated]


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            json_data = json.dumps(serializer.data)
            response = TransactionFactory.transaction_selector(json_data)
            print(response.status_code)
            if response.status_code == 200:
                data = {
                    'serviceCode': 'WBB',
                    'request_id': str(uuid.uuid4()),
                    'reference': response.json().get('reference')
                }
                json_data = json.dumps(data)
                print(json_data)
                response = TransactionFactory.transaction_selector(json_data) 
                print(response.json())
                return Response(response.json(), status=response.status_code)
            # raise serializers.ValidationError()
            

class VTUView(generics.CreateAPIView):
    serializer_class = VTUSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            print(serializer)
            data = {
                'serviceCode': serializer.data['serviceCode'],
                'amount' : serializer.data['amount'],
                'phone': serializer.data['phone'],
                'vend_type': serializer.data['vend_type'],
                'network': serializer.data['network'],
                'request_id': str(uuid.uuid4())
            }
            json_data = json.dumps(data)
            response = AirtimeDataFactory.check_transaction_type(json_data)
            return Response(response.json(), status=response.status_code)



            
        
    
