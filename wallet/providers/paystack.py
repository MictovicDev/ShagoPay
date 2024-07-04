from .baseprovider import BaseProvider
import os
import requests


class PayStackProvider(BaseProvider):
    def verify_payment(self):
        return super().verify_payment()
    
    def money_transfer(self, headers,payload):
        url = 'https://api.paystack.co/transaction/initialize'
        response = requests.post(url, headers=headers, data=payload)
        return response

    def get_headers(self):
        paystack_secret = os.getenv('PAYSTACK_SECRET')
        headers = {
            "Authorization": f"Bearer {paystack_secret}",
            "Content-Type": "application/json"
        }
        return headers

    