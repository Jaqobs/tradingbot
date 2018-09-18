from exchange import ExchData
import tradelogic
import indicators
import time
import mexorders as bitmex


def main():

	bfx = ExchData('bfx', 'BTC/USDT')
	sleep_timer = 3600 #3600sec = 1h

	while True:
		bfx.clear_candles()
		bfx.fetch_candles_long(timeframe='1h', start=52, limit=624)
		candles = bfx.get_candles()
		converted_candles = bfx.convert_candles(candles, 4)

		candle_open = []
		candle_close = []
		volume = []
		for candle in converted_candles:
			candle_open.append(candle['open'])
			candle_close.append(candle['close'])
			volume.append(candle['volume'])
		
		if (tradelogic.long_open(candle_open, candle_close)) and (bitmex.has_orders() == False):
			bitmex.create_order('limit', 'buy', 1, 1000)

		if (tradelogic.long_close(candle_open, candle_close)) and (bitmex.has_orders() == True):
			bitmex.create_order('limit', 'sell', 1, 1000)

		if (tradelogic.short_open(candle_open, candle_close)) and (bitmex.has_orders() == False):
			bitmex.create_order('limit', 'sell', 1, 10000)

		if (tradelogic.short_close(candle_open, candle_close)) and (bitmex.has_orders() == True):
			bitmex.create_order('limit', 'buy', 1, 1000)

		print('Waiting for next cycle.')
		time.sleep(sleep_timer * 2)	#4 hours
	
if __name__ == '__main__':
	main()