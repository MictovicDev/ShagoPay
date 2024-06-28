from django.db import models
from authentication.models import User

# Create your models here.




class Wallet(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.PositiveBigIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.owner.__str__()
    

class FundWallet(models.Model):
    amount = models.PositiveBigIntegerField(default=100)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.wallet} Funded {self.amount} "


    
class WalletTransactions(models.Model):

    TRANSACTION_TYPES = (
        ('deposit', 'deposit'),
        ('transfer', 'transfer'),
        ('withdraw', 'withdraw'),
    )

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    transaction_type = models.CharField(
        max_length=200, null=True,  choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=100, null=True, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, default="pending")
    paystack_payment_reference = models.CharField(max_length=100, default='', blank=True)

    
    def __str__(self):
        return self.wallet.__str__()


