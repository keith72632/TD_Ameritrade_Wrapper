import requests
import os

class Market:
    def __init__(self, symbol):
        self.symbol = symbol
        self.key = os.environ.get('CONSUMER_KEY')

    def get_movers(self, **kwargs):
        url = os.environ.get('TD_API_MOVERS').format(kwargs.get('symbol'))

        params = {}
        params.update({'apikey': self.key})

        for arg in kwargs:
            parameter = {arg: kwargs.get(arg)}
            params.update(parameter)
        
        return requests.get(url, params=params).json()