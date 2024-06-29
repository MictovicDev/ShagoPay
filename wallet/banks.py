from abc import ABC, abstractmethod
import requests


class BankPayment(ABC):

    @abstractmethod
    def initialize_transaction(self):
        pass


class AccountValidation(ABC):
    def initialize_transaction(self, data):
        url = 'http://test.shagopayments.com/public/api/test/b2b'
        email = 'test@shagopayments.com'
        password = 'test123'
        headers = {
            "Content-Type": "application/json",
            "email": email,
            "password": password
        }
        response = requests.post(url, headers=headers, data=data)
        return response.json()

class SendMoney(ABC):
    
    def initialize_transaction(self):
        pass

class ListBanks(ABC):
    
    def initialize_transactions(self):
        pass


class TransactionFactory:

    @staticmethod
    def transaction_selector(service_code):
        if service_code == 'WBV':
            AccountValidation.validate_account()

        