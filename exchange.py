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
		else:
			exchange == ccxt.bitfinex2()
		print('Connection to {0} established...'.format(self.exchange.describe()['name']))

		self.symbol = symbol
		print('Symbol: {}'.format(self.symbol))
		
		self.candles = []
			

	def get_books(self, symbol, ):
		book = self.exchange.fetch_order_book(self.symbol)


	def clear_candles(self):
		self.candles = []
		print('Candles cleared...')
			
	def fetch_candles(self, timeframe=None, start=None, limit=None):
		print('Attempting to fetch candles...')
		if timeframe == None:
			timeframe = '1h'
		print('Timeframe: {}'.format(timeframe))

		if start == None:
			start = int(self.exchange.milliseconds()) - 86400000 * 1 #last 1 * 24hours
		else:
			start = int(self.exchange.milliseconds()) - 86400000 * start
		print('Start date: {}'.format(self.exchange.iso8601(start)))

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
		print('Start date: {}'.format(self.exchange.iso8601(since)))

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
		print('Start date: {}'.format(self.exchange.iso8601(since)))
		results2 = results = self.exchange.fetch_ohlcv(self.symbol, timeframe=timeframe, since=since, limit=limit)

		for element in results2:
			candle = {
				'timestamp':element[0],
				'open':element[1],
				'high':element[2],
				'low':element[3],
				'close':element[4],
				'volume':element[5]
				}

			self.candles.insert(0, candle)


	def get_candles(self):
		return self.candles


	def get_hour(self, timestamp):
		hour = datetime.datetime.utcfromtimestamp(timestamp / 1000).strftime('%H')		#take timestamp and remove miliseconds

		return hour


	def convert_candles(self, candle_data, timeframe):
		new_candles = []
		condition = True
		
		#remove open candles
		print('Original length: {}'.format(len(candle_data)))		#debugging
		while (condition): 		
			if ( int(self.get_hour(candle_data[0]['timestamp'])) % 4 == 0 ):
				condition = False
			else:
				del candle_data[0]
		print('New length: {}'.format(len(candle_data)))		#debugging
		
		#create custom candles
		i = 0
		for i in range(i, len(candle_data) - len(candle_data)%timeframe, timeframe):
			candle_timestamp = candle_data[i]['timestamp']
			candle_open = candle_data[i]['open']

			candle_high = min(
							candle_data[i]['high'],
							candle_data[i+1]['high'],
							candle_data[i+2]['high'],
							candle_data[i+3]['high']
							)

			candle_low = min(
							candle_data[i]['low'],
							candle_data[i+1]['low'],
							candle_data[i+2]['low'],
							candle_data[i+3]['low']
							)

			candle_close = candle_data[i+3]['close']

			candle_volume = int(candle_data[i]['volume']) \
							+ int(candle_data[i+1]['volume']) \
							+ int(candle_data[i+2]['volume']) \
							+ int(candle_data[i+3]['volume']) 

			candle = {
				'timestamp':candle_timestamp,
				'open':candle_open,
				'high':candle_high,
				'low':candle_low,
				'close':candle_close,
				'volume':candle_volume
				}

			new_candles.append(candle)

		return new_candles