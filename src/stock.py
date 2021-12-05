import requests
import os
import config

class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.key = config.consumer_key

    """possible arguments: period(integer, how many of specified period types), periodType(string, day month year etc), frequencyType(string minute hour day etc within periodType), 
        frequency(integer, number of the frequency type in each candle)
    """
    def get_price_history(self, **kwargs):
        url = 'https://api.tdameritrade.com/v1/marketdata/{}/pricehistory'.format(self.symbol)

        params = {}
        params.update({'apikey': self.key})

        for arg in kwargs:
            parameter = {arg: kwargs.get(arg)}
            params.update(parameter)
        
        
        res = requests.get(url, params=params)
        return res.json()

    #real time quote
    def get_quote(self):
        url = 'https://api.tdameritrade.com/v1/marketdata/{}/quotes'.format(self.symbol)

        params = {}
        params.update({'apikey': self.key})

        
        res = requests.get(url, params=params)
        return res.json()