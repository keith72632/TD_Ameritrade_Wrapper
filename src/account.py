import requests
import os
import config

class Account:
    def __init__(self):
        self.account_no = os.environ.get('TD_ACCOUNT')
        self.key = config.consumer_key

    def get_positions(self):
        # url = 'https://api.tdameritrade.com/v1/accounts/{}'.format(self.account_no)
        # params = {}
        # params.update({'apikey': self.key})
        # params.update({'fields': 'positions'})
        

        # return requests.get(url, params=params).json()
        pass