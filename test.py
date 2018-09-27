import configparser
import ccxt
import time

cp = configparser.RawConfigParser()  
cp.read('config.txt')
apilimit = 5
apisleep = 5
bitmex = ccxt.bitmex({
					'apiKey': cp.get('bitmex', 'APIKEY'),
					'secret': cp.get('bitmex', 'SECRET'),
					})
			
def last_price(symbol):
	ticker = bitmex.fetch_ticker(symbol)
	print('Last price: {}'.format(ticker['last']))

	return ticker['last']

last_price('BTC/USD')