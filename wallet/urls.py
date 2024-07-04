from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [
   path('funds', views.FundWalletView.as_view(), name="fundwallet"),
   path('transfers', views.ShagoMoneyTransferView.as_view(), name="transfer"),
   path('vtu', views.ShagoAirtimeView.as_view(), name='vtu')
]