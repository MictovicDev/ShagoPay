from .baseprovider import BaseProvider
import os
import requests
import uuid
import json


class ShagoProvider(BaseProvider):
    def verify_payment(self):
        return super().verify_payment()

    def buy_airtime(self, payload, headers):
        url = 'http://test.shagopayments.com/public/api/test/b2b'
        payload['request_id'] = str(uuid.uuid4())
        json_data = json.dumps(payload)
        response = requests.post(url, headers=headers, data=json_data)
        return response

    def money_transfer(self, headers, payload):
        url = 'http://test.shagopayments.com/public/api/test/b2b'
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200:
                data = {
                    'serviceCode': 'WBB',
                    'request_id': str(uuid.uuid4()),
                    'reference': response.json().get('reference')
                }
                json_data = json.dumps(data)
                response = requests.post(url, headers=headers, data=json_data)
                return response

    def get_headers(self):
        email = os.getenv('SHAGO_EMAIL')
        password = os.getenv('SHAGO_PASSWORD')
        hash_key = os.getenv('SHAGO_HASH_KEY')
        headers = {
            "Content-Type": "application/json",
            "email": email,
            "password": password,
            "hash_key": hash_key
        }
        return headers
        
