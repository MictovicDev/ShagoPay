from abc import ABC, abstractmethod
import json
import requests


class VTUManager(ABC):
    @abstractmethod
    def initialize_transaction(self):
        pass

class Data(VTUManager):
    def initialize_transaction(self):
        pass

class Airtime(VTUManager):
    def initialize_transaction(self, json_data):
        try:
            url = 'http://test.shagopayments.com/public/api/test/b2b'
            email = 'test@shagopayments.com'
            password = 'test123'
            hash_key = 'c1df88d180d0163fc53f4efde6288a2c87a2ceaaefae0685fd4a8c01b217e70d'
            headers = {
                "Content-Type": "application/json",
                "email": email,
                "password": password,
                "hash_key": hash_key
            }
            response = requests.post(url, headers=headers, data=json_data)
            print(response.json())
            return response
        except Exception as e:
            print(f"Error in SendMoney: {e}")

class AirtimeDataFactory:
    @staticmethod
    def check_transaction_type(json_data):
        j_son = json.loads(json_data)
        if j_son['serviceCode'] == 'QAB':
            transaction =  Airtime()
            response = transaction.initialize_transaction(json_data)
            return response
        if j_son['serviceCode'] == 'WBB':
            print(j_son)
            data = Data()
            response = data.initialize_transaction(json_data)
            return response
        return None