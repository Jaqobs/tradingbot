import configparser
import bitmex
import datetime
import time
from dateutil import tz


def get_auth(arg):
	x = ''
	configParser = configparser.RawConfigParser()   
	configParser.read('config.txt')
	
	try:
		x = configParser.get('bitmex', arg)
	except:
		print('invalid config file')

	return x

def order(size=None, price=None, ordertype=None):
	if size == None:
		size = 0
	if price == None:
		price = 0
	if ordertype == None:
		ordertype = 'limit'

def time_conversion(args):
	from_zone = tz.tzutc()
	to_zone = tz.tzlocal()
	utc = args.replace(tzinfo=from_zone)
	time = utc.astimezone(to_zone)
	
	return time

def request_funding(client):
	result = client.Funding.Funding_get(symbol='XBTUSD', reverse=True, count=1).result()
	
	print('Funding is: {0:.4f}%. Funding in __ hours'.format(result[0][0]['fundingRate'] * 100))
	

def request_instrument(client, symbol=None, li=None):
	if symbol == None:
		symbol = 'XBTUSD'

	result = client.Instrument.Instrument_get(symbol=symbol, reverse=True).result()
	if li is not None:
		for word in li:
			try:
				print('{}: {}'.format(word, result[0][0][word]))
			except:
				print('Does not exist')
				continue
			

def main():
	client = bitmex.bitmex(test=False, api_key=get_auth('APIKEY'), api_secret=get_auth('SECRET'))
	
	request_instrument(client, li=('highPrice', 'lowPrice', 'lastPrice'))
	request_funding(client)

if __name__ == "__main__":
	main()
