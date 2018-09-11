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

			
	def fetch_candles(self, timeframe=None, start=None, limit=None):
		print('Attempting to fetch candles...')
		if timeframe == None:
			timeframe = '1h'
		print('Timeframe: {}'.format(timeframe))

		if start == None:
			start = int(self.exchange.milliseconds()) - 86400000 * 1 #last 1 * 24hours
		else:
			start = int(self.exchange.milliseconds()) - 86400000 * start
		print('Start date: {}'.format(start))

		if limit == None:
			limit = 100
		print('Limit: {}'.format(limit))

		results = self.exchange.fetch_ohlcv(self.symbol, timeframe=timeframe, since=start, limit=limit)

		for element in results:
			candle = {
				'timestamp':element[0],
				'open':element[1],
				'high':element[2],
				'low':element[3],
				'close':element[4],
				'volume':element[5]}

			self.candles.insert(0, candle)


	def fetch_candles_long(self, timeframe, start, limit):
		print('Attempting to fetch candles...')
		print('Timeframe: {}'.format(timeframe))

		since = int(self.exchange.milliseconds()) - 86400000 * start
		print('Start date: {}'.format(since))

		if limit == None:
			limit = 1000
		print('Limit: {}'.format(limit))

		results = self.exchange.fetch_ohlcv(self.symbol, timeframe=timeframe, since=since, limit=limit)

		for element in results:
			candle = {
				'timestamp':element[0],
				'open':element[1],
				'high':element[2],
				'low':element[3],
				'close':element[4],
				'volume':element[5]}

			self.candles.insert(0, candle)

		print('Fetching second part of candles...')
		since = int(self.exchange.milliseconds()) - 86400000 * int(start // 2)
		print(since)
		results2 = results = self.exchange.fetch_ohlcv(self.symbol, timeframe=timeframe, since=since, limit=limit)

		for element in results2:
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


