import configparser
import ccxt
import datetime
import time
from dateutil import tz

cp = configparser.RawConfigParser()  
cp.read('config.txt')

apitry = 0
apilimit = 20
apisleep = 5
bitmex = None
while (apitry < apilimit) and not bitmex:
	try:
		bitmex = ccxt.bitmex({
								'apiKey': cp.get('bitmex', 'APIKEY'),
								'secret': cp.get('bitmex', 'SECRET'),
								})
		print('Connection to bitmex established.')
	except(ccxt.ExchangeError):
		print('Could not establish connection. Trying again...')
		apitry += 1
		time.sleep(apisleep)

symbol = u'BTC/USD'
			

def create_order(ordertype, side, amount, price):
	apitry = 0
	while (apitry < apilimit):
		try:
			bitmex.create_order(symbol=symbol, type=ordertype, side=side, amount=float(amount), price=float(price))
			print('{} order successfully created! {} {} at {}\n'.format(ordertype, side, amount, price))
		except(ccxt.ExchangeError):
			print('Error. Could not create order.')
			apitry += 1
			time.sleep(apisleep)


def get_positions_all():
	positions = []
	try:
		bitmex.private_get_position()
	except(ccxt.ExchaneError):
		print('Error. Could not fetch positions.')
	
	return positions


def get_open_orders():
	orders = []
	try:
		orders = bitmex.fetch_open_orders(symbol=symbol)
	except(ccxt.ExchangeError):
		print('Error. Could not fetch orders.')

	return orders


def has_orders():
	orders = get_open_orders()
	if not orders:
		return False
	else:
		return True

def cancel_all_orders():
	apitry = 0
	orders = get_open_orders()
	if orders:
		for order in orders:
			while (apitry < apilimit):
				try:
					print('Cancel order with ID: {}'.format(order['id']))
					bitmex.cancel_order (order['id'])
				except(ccxt.ExchangeError):
					print('Error.')
					apitry += 1
					time.sleep(apisleep)

		print('All orders canceled.')
	else:
		print('No open orders.')


