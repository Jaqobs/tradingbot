import configparser
import ccxt
import time
import logging

cp = configparser.RawConfigParser()  
cp.read('config.txt')
apilimit = 5
apisleep = 5
bitmex = ccxt.bitmex({
					'apiKey': cp.get('bitmex', 'APIKEY'),
					'secret': cp.get('bitmex', 'SECRET'),
					})
			
def create_order(symbol, ordertype, side, amount, price=None):
	apitry = 0
	condition = True

	if (symbol == 'XBTUSD'):
		symbol = 'BTC/USD'

	while (apitry < apilimit) and (condition):
		try:
			order = bitmex.create_order(symbol=symbol, type=ordertype, side=side, amount=amount, price=price)
			logging.info('Order successfully created!')
			logging.info(order)
			condition = False
		except(ccxt.ExchangeError):
			logging.error('Could not create order. Trying again...')
			apitry += 1
			time.sleep(apisleep)


def get_last_price(symbol):
	apitry = 0
	condition = True
	while (condition) and (apitry < apilimit):
		try:
			ticker = bitmex.fetch_ticker(symbol)
			condition = False
		except:
			logging.error('Timeout. Trying again...')
			apitry += 1
			time.sleep(apisleep)
			
	logging.info('Last price: {}'.format(ticker['last']))

	return ticker['last']


def get_all_positions():
	apitry = 0
	positions = []
	condition = True
	while (condition) and (apitry < apilimit):
		try:
			positions = bitmex.private_get_position()
			condition = False
		except(ccxt.ExchangeError):
			logging.error('Could not fetch positions. Trying again...')
			apitry += 1
			time.sleep(apisleep)
	
	return positions


def get_open_position(symbol):
	open_position = []
	positions = get_all_positions()
	if symbol == 'BTC/USD':
		symbol = 'XBTUSD'
	
	for position in positions: 
		if (int(position['currentQty']) is not 0) and (position['symbol'] == symbol):
			open_position.append(position)

	return open_position


def get_all_open_positions():
	open_positions = []
	positions = get_all_positions()

	for position in positions: 
		if (int(position['currentQty']) is not 0):
			open_positions.append(position)

	return open_positions


def has_position():
	positions = get_all_open_positions()
	if (positions):
		logging.info('Is currently in position.')
		return True
	else:
		logging.info('Is currently NOT in position...')
		return False


def has_long_position(symbol):
	position = get_open_position(symbol)
	if (position):
		if (int(position[0]['currentQty']) > 0):
			logging.info('Is currently in LONG position.')
			return True
	else:
		logging.info('Is currently NOT in LONG position...')
		return False


def has_short_position(symbol):
	position = get_open_position(symbol)
	if (position):
		if (int(position[0]['currentQty']) < 0):
			logging.info('Is currently in SHORT position.')
			return True
	else:
		logging.info('Is currently NOT in SHORT position...')
		return False


def get_open_orders():
	apitry = 0
	condition = True
	orders = []

	while (condition) and (apitry < apilimit):
		try:
			orders = bitmex.fetch_open_orders()
			condition = False
		except(ccxt.ExchangeError):
			logging.error('Could not fetch orders.')
			apitry += 1
			time.sleep(apisleep)

	return orders


def has_orders():
	orders = get_open_orders()
	if (orders):
		logging.info('Has orders.')
		return True
	else:
		logging.info('Has NO orders.')
		return False


def cancel_order(orderid):
	apitry = 0
	condition = True

	while (apitry < apilimit) and condition: 
		try:
			bitmex.cancel_order(orderid)
			condition = False
		except:
			logging.error('Could not cancel order. Trying again...')
			apitry += 1
			time.sleep(apisleep)


def cancel_all_orders():
	orders = get_open_orders()
	if orders:
		for order in orders:
			cancel_order (order['id'])

		logging.warning('All orders canceled.')
	else:
		logging.warning('No open orders.')


def close_position(symbol):
	position = get_open_position(symbol)
	if (position):
		if (int(position[0]['currentQty']) > 0):
			side = 'sell'
		elif (int(position[0]['currentQty']) < 0):
			side = 'buy'
		amount = float(position[0]['currentQty']) * -1
		if symbol == 'XBTUSD':
			symbol = 'BTC/USD'
		

		logging.warning('Attempting to close position: {}'.format(position[0]['symbol']))
		logging.warning('Side: {} -- Quantity: {} -- Symbol: {}'.format(side, amount, symbol))
		create_order(symbol,'market', side, amount)
		logging.warning('Position {} closed.'.format(symbol)) 
	else:
		logging.warning('No position with instrument {} open'.format(symbol))


def close_all_positions():
	positions = get_all_open_positions()
	if (positions):
		for position in positions:
			close_position(position[0]['symbol'])

		logging.warning('All open positions closed.')
	else:
		logging.warning('No open positions')

