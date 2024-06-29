from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [
   path('fund', views.FundWalletView.as_view(), name="fundwallet"),
   path('transfer', views.B2BTransferView.as_view(), name="transfer")
]