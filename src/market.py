import requests
import os
import config

class Market:
    def __init__(self, symbol):
        self.symbol = symbol
        self.key = config.consumer_key

    def get_movers(self, **kwargs):
        url = 'https://api.tdameritrade.com/v1/marketdata/{}/movers'.format(kwargs.get('symbol'))

        params = {}
        params.update({'apikey': self.key})

        for arg in kwargs:
            parameter = {arg: kwargs.get(arg)}
            params.update(parameter)
        
        return requests.get(url, params=params).json()