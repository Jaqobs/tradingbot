#tradelogic by Jaqobs
#4h strategy

import indicators as ind
import logging

def long_open(candle_low, candle_close, volume):
	boolean = False
	bottom_band = ind.vwma(candle_close, volume, 200) * 0.966235

	logging.info('Current low: {0} - Long Entry: {1:.2f}'.format(candle_low[0], bottom_band))

	if (candle_low[0] < bottom_band):
		boolean = True	
	
	logging.info('Long open: {}'. format(boolean))

	return boolean


def long_close(candle_high, candle_close, volume):
	boolean = False
	close = ind.vwma(candle_close, volume, 200) * 1.004882

	logging.info('Long close at {0:.2f}'.format(close))

	if (candle_high[0] > close):
		boolean = True

	logging.info('Long close: {}'. format(boolean))

	return boolean


def short_open(candle_high, candle_close, volume):
	boolean = False
	top_band = ind.vwma(candle_close, volume, 200) * 1.036117
	
	logging.info('Current high {0} - Short Entry: {1:.2f}'.format(candle_high[0], top_band))

	if (candle_high[0] > top_band):
		boolean = True	
	
	logging.info('Short open: {}'. format(boolean))

	return boolean


def short_close(candle_low, candle_close, volume):
	boolean = False
	close = ind.vwma(candle_close, volume, 200) * 0.995117

	logging.info('Short close at {0:.2f}'.format(close))

	if (candle_low[0] < close):
		boolean = True

	logging.info('Short close: {}'. format(boolean))

	return boolean