#tradelogic by Jaqobs
#4h strategy

import indicators as ind
import logging

def long_open(data_open, data_close):
	current_price = 0.0
	alma_close = ind.alma(data_close, 300)
	ema_close = ind.ema(data_close, 9)
	ema_open = ind.ema(data_open, 9)
	boolean = False

	logging.info('9Ema Close: {} - 9Ema Open: {} - 300Alma: {}'.format(ema_close, ema_open, alma_close))

	if (ema_close > alma_close) and (ema_open < alma_close):
		boolean = True	
	
	logging.info('Long open: {}'. format(boolean))

	return boolean


def long_close(data_open, data_close):
	current_price = 0.0
	ema_thirty_close = ind.ema(data_close, 30)
	ema_close = ind.ema(data_close, 9)
	ema_open = ind.ema(data_open, 9)
	boolean = False

	logging.info('9Ema: {} - 30Ema: {}'.format(ema_close, ema_thirty_close))

	if (ema_close < ema_thirty_close) and (ema_open > ema_thirty_close):
		boolean = True

	logging.info('Long close: {}'. format(boolean))

	return boolean


def short_open(data_open, data_close):
	current_price = 0.0
	alma_close = ind.alma(data_close, 300)
	ema_close = ind.ema(data_close, 9)
	ema_open = ind.ema(data_open, 9)
	boolean = False

	logging.info('9Ema Close: {} - 9Ema Open: {} - 300Alma: {}'.format(ema_close, ema_open, alma_close))

	if (ema_close < alma_close) and (ema_open > alma_close):
		boolean = True
	
	logging.info('Short open: {}'. format(boolean))
	
	return boolean


def short_close(data_open, data_close):
	current_price = 0.0
	ema_thirty_close = ind.ema(data_close, 30)
	ema_close = ind.ema(data_close, 9)
	ema_open = ind.ema(data_open, 9)
	boolean = False

	logging.info('9Ema: {} - 30Ema: {}'.format(ema_close, ema_thirty_close))

	if (ema_close > ema_thirty_close) and (ema_open < ema_thirty_close):
		boolean = True
		
	logging.info('Short close: {}'. format(boolean))
	
	return boolean