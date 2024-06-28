from abc import ABC, abstractmethod


class BankPayment(ABC):

    @abstractmethod
    def make_transactions(self):
        pass


class ShagoBankPayment(ABC):

    def make_transactions(self):
        pass

class PayStackBankPayment(ABC):
    
    def make_transactions(self):
        pass

class FlutterBankPayment(ABC):
    
    def make_transactions(self):
        pass


class PaymentFactory:

    @abstractmethod
    def transaction_selector(transaction):
        pass

        