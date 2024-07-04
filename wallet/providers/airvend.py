from .baseprovider import BaseProvider
import os
import requests
import hashlib
# hash = sha512 ( json_body + api_key)

class AirVendProvider(BaseProvider):
    def verify_payment(self):
        return super().verify_payment()
    
    
    def money_transfer(self):
        pass

    def vtu_transactions(self):
        pass

    def get_headers(self):
        email = os.getenv('AIRVEND_EMAIL')
        password = os.getenv('AIRVEND_PASSWORD')
        hash_key = os.getenv('AIRVEND_HASH_KEY')
        headers = {
            "Content-Type": "application/json",
            "email": email,
            "password": password,
            "hash_key": hash_key
        }
        return headers
        

		

				
