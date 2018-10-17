import time
import indicators
from exchange import ExchData
import ordermanager as bitmex
import tradelogic
import logging
import sys

def main():
	logging.basicConfig( 
		level = logging.INFO,
		format = '%(asctime)s  %(levelname)-10s %(processName)s  %(name)s %(message)s',
		handlers=[
			logging.FileHandler('{1}.log'.format(sys.path[0], time.strftime("test-%Y-%m-%d"))),
			logging.StreamHandler()
			]
		)
	logging.info('Test started.')

	bfx = ExchData('ETH/USDT')
	sleep_timer = 60 #3600sec = 1h
	symbol = 'ETH/USD'
	while True:
		bfx.clear_candles()
		bfx.fetch_candles(timeframe='5m', start=1, limit=1000)
		candles = bfx.get_candles()

		candle_open = []
		candle_high = []
		candle_low = []
		candle_close = []
		volume = []
		
		for candle in candles:
			candle_open.append(candle['open'])
			candle_high.append(candle['high'])
			candle_low.append(candle['low'])
			candle_close.append(candle['close'])
			volume.append(candle['volume'])

		mid_line = indicators.vwma(candle_close, volume, 200)
		lastPrice = bitmex.get_last_price(symbol)

		logging.info('VWMA: {0:.2f}'.format(mid_line))

		if (tradelogic.long_open(candle_low, candle_close, volume)):
			logging.warning('Long opened at {}'.format(lastPrice))
		if (tradelogic.long_close(candle_high, candle_close, volume)):
			logging.warning('Long closed at {}'.format(lastPrice))
		if (tradelogic.short_open(candle_high, candle_close, volume)):
			logging.warning('Short opened at {}'.format(lastPrice))
		if (tradelogic.short_close(candle_low, candle_close, volume)):
			logging.warning('Short closed at {}'.format(lastPrice))


		

		logging.info('Waiting for next cycle...')
		logging.info('-------------')
		time.sleep(sleep_timer * 5)
	
if __name__ == '__main__':
	main()