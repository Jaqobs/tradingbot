import configparser
import requests
import ccxt
import time
import indicators
from exchange import ExchData
import ordermanager as bitmex
import logging

cp = configparser.RawConfigParser()  
cp.read('config.txt')
apilimit = 5
apisleep = 5
bitmex = ccxt.bitmex({
                    'apiKey': cp.get('bitmex', 'APIKEY'),
                    'secret': cp.get('bitmex', 'SECRET'),
                    })

def get_funding(symbol):
    funding = {}
    url = 'https://www.bitmex.com/api/v1/instrument?'

    params = dict(
        symbol=symbol,
        count='1',
        reverse='true',
    )

    resp = requests.get(url=url, params=params)
    data = resp.json() # Check the JSON Response Content documentation below
    
    funding['symbol'] =  data[0]['symbol']
    funding['fundingTimestamp'] = data[0]['fundingTimestamp']
    funding['fundingRate'] = data[0]['fundingRate']
    funding['indicativeFundingRate'] = data[0]['indicativeFundingRate']

    return funding


def main():
    #a = bitmex.public_get_instrument('XBTUSD')
    a = get_funding('ETHUSD')
    print(a)
    

if __name__ == '__main__':
    main()