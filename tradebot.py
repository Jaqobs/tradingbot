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
	#bfx.fetch_candles_long(timeframe='1h', start=50, limit=600)
	bfx.fetch_candles(timeframe='1h', start=20, limit=100)
	candles = bfx.get_candles()

	while True:
		print('Counting candles...')
		print(len(candles))
		candle_open = []
		candle_close = []
		for candle in candles:
			candle_open.append(candle['open'])
			candle_close.append(candle['close'])

		print('Long open: {}'.format(tradelogic.long_close(candle_open, candle_close)))
		#print('Ema 9: {}'.format(ema(candle_close, 9)))

		time.sleep(14400)	#4 hours
	
if __name__ == '__main__':
	main()