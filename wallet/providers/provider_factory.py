from .shago import ShagoProvider
from .airvend import AirVendProvider
from .paystack import PayStackProvider
import json

class ProviderFactory:
    """Used to Create Different Providers in Runtime"""
    @staticmethod
    def createprovider(type):
        # data = json.loads(payload)
        if type == 'shago':
            return ShagoProvider()
        if type == 'FUND':
            return PayStackProvider()
           



