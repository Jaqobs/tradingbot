#tradelogic by Jaqobs
import indicators

def main():

def long_open():
	data_open = []
	data_cose = []
	current_price = 0.0
	alma_close = alma(data_close, 50)
	ema_close = ema(data_close, 9)
	ema_open = ema(data_open, 9)
	boolean = False

	if (ema_close > alma_close) and (ema_open < alma_close):
		boolean = True

	return boolean


def long_close():
	data_open = []
	data_cose = []
	current_price = 0.0
	ema_thirty_close = ema(data_close, 30)
	ema_close = ema(data_close, 9)
	ema_open = ema(data_open, 9)
	boolean = False

	if (ema_close < ema_thirty_close) and (ema_open > ema_thirty_close):
		boolean = True

	return boolean


def short_close():
	data_open = []
	data_cose = []
	current_price = 0.0
	alma_close = alma(data_close, 50)
	ema_close = ema(data_close, 9)
	ema_open = ema(data_open, 9)
	boolean = False

	if (ema_close < alma_close) and (ema_open > alma_close):
		boolean = True

	return boolean


def short_close():
	data_open = []
	data_cose = []
	current_price = 0.0
	ema_thirty_close = ema(data_close, 30)
	ema_close = ema(data_close, 9)
	ema_open = ema(data_open, 9)
	boolean = False

	if (ema_close > ema_thirty_close) and (ema_open < ema_thirty_close):
		boolean = True

	return boolean