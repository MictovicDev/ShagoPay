from abc import ABC, abstractmethod
import requests
import json
import os

class BankPayment(ABC):

    @abstractmethod
    def initialize_transaction(self,data):
        pass


class AccountValidation(BankPayment):
    def __init__(self):
        pass
        
    def initialize_transaction(self, json_data):
        try:
            url = 'http://test.shagopayments.com/public/api/test/b2b'
            email = os.getenv('EMAIL')
            password = os.getenv('PASSWORD')
            hash_key = os.getenv('HASH_KEY')
            headers = {
                "Content-Type": "application/json",
                "email": email,
                "password": password,
                "hash_key": hash_key
            }
            response = requests.post(url, headers=headers, data=json_data)
            return response
        except Exception as e:
            print(f"Error in SendMoney: {e}")
            

class SendMoney(BankPayment):
    def __init__(self):
        pass
       
    def initialize_transaction(self, json_data):
        try:
            url = 'http://test.shagopayments.com/public/api/test/b2b'
            email = os.getenv('EMAIL')
            password = os.getenv('PASSWORD')
            hash_key = os.getenv('HASH_KEY')
            headers = {
                "Content-Type": "application/json",
                "email": email,
                "password": password,
                "hash_key": hash_key
            }
            response = requests.post(url, headers=headers, data=json_data)
            return response
        except Exception as e:
            print(f"Error in SendMoney: {e}")
            
       

class ListBanks(BankPayment):
    def initialize_transaction(self, json_data):
        try:
            url = 'http://test.shagopayments.com/public/api/test/b2b'
            email = os.getenv('EMAIL')
            password = os.getenv('PASSWORD')
            hash_key = os.getenv('HASH_KEY')
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


class TransactionFactory:
    @staticmethod
    def transaction_selector(json_data):
        j_son = json.loads(json_data)
        if j_son['serviceCode'] == 'WBV':
            transaction =  AccountValidation()
            response = transaction.initialize_transaction(json_data)
            return response
        if j_son['serviceCode'] == 'WBB':
            print(j_son)
            sendmoney = SendMoney()
            response = sendmoney.initialize_transaction(json_data)
            return response
        return None
        

        