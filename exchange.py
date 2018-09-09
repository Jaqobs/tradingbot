import configparser
import ccxt
import datetime
import time
from dateutil import tz

class ExchData():
	cp = configparser.RawConfigParser()  
	cp.read('config.txt')

	def __init__(self, exchange, symbol, ):
		if exchange == 'bfx':
			self.exchange = ccxt.bitfinex2({
				'rateLimit': 10000,
			'enableRateLimit': True
		})
		elif exchange == 'bitmex':
			self.exchange = ccxt.bitmex()
		else:
			exchange == ccxt.bitfinex2()
		print('Connection to {0} established...'.format(self.exchange.describe()['name']))

		self.symbol = symbol
		print('Symbol: {}'.format(self.symbol))
		
		self.candles = []
			

	def get_books(self, symbol, ):
		book = self.exchange.fetch_order_book(self.symbol)

			
	def fetch_candles(self, timeframe=None, start=None, end=None, limit=None):
		print('Attempting to fetch candles...')
		if timeframe == None:
			timeframe = '1h'
		print('Timeframe: {}'.format(timeframe))

		if start == None:
			start = int(self.exchange.milliseconds()) - 86400000 * 7 #last 1 * 24hours
		print('Start date: {}'.format(start))

		if limit == None:
			limit = 10
		print('Limit: {}'.format(limit))

		#self.candles = self.exchange.fetch_ohlcv(self.symbol, timeframe, start, limit, params={'sort': -1})
		#self.candles = self.exchange.fetch_ohlcv(self.symbol, timeframe=timeframe, since=start, limit=limit, params={'sort': -1})
		results = self.exchange.fetch_ohlcv(self.symbol, timeframe=timeframe, since=start, limit=limit, params={'sort': -1})

		for element in results:
			candle = {
				'timestamp':element[0],
				'open':element[1],
				'high':element[2],
				'low':element[3],
				'close':element[4],
				'volume':element[5]}

			self.candles.insert(0, candle)


	def get_candles(self):
		return self.candles

def main():

	#bitmex = ccxt.bitmex({
	#		'apiKey': cp.get('bitmex', 'APIKEY'),
	#    	'secret': cp.get('bitmex', 'SECRET'),
	#    	})

	btcusd = 'BTC/USDT'
	bfx = ExchData('bfx', btcusd)
	bfx.fetch_candles(timeframe='6h')
	candles = bfx.get_candles()

	print('Printing candles...')
	for candle in candles:
		print(candle)
		print('----')
	#while True:
	

if __name__ == "__main__":
	main()
