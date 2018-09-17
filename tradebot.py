from exchange import ExchData
import tradelogic
import indicators
import time


def main():

	#bitmex = ccxt.bitmex({
	#		'apiKey': cp.get('bitmex', 'APIKEY'),
	#    	'secret': cp.get('bitmex', 'SECRET'),
	#    	})

	btcusd = 'BTC/USDT'
	bfx = ExchData('bfx', btcusd)
	bfx.fetch_candles_long(timeframe='1h', start=120, limit=960)
	#bfx.fetch_candles(timeframe='1h', start=20, limit=100)
	candles = bfx.get_candles()

	while True:
		print('Counting candles...')
		print(len(candles))
		converted_candles = bfx.convert_candles(candles, 4)
		print('{} candles returned.'.format(len(converted_candles)))

		candle_open = []
		candle_close = []
		for candle in converted_candles:
			candle_open.append(candle['open'])
			candle_close.append(candle['close'])
		
		print('Long open: {}\n'.format(tradelogic.long_open(candle_open, candle_close)))
		print('Long close: {}\n'.format(tradelogic.long_close(candle_open, candle_close)))
		print('Short open: {}\n'.format(tradelogic.short_open(candle_open, candle_close)))
		print('Short close: {}\n'.format(tradelogic.short_close(candle_open, candle_close)))
		#print('Ema 9: {}'.format(ema(candle_close, 9)))

		time.sleep(14400)	#4 hours
	
if __name__ == '__main__':
	main()