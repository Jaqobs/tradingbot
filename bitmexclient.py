import configparser
import bitmex
import datetime
from dateutil import tz


def get_auth(arg):
	x = ''
	configParser = configparser.RawConfigParser()   
	configParser.read('config.txt')
	
	try:
		x = configParser.get('login', arg)
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

def get_funding(client, request=None):
	if request == None:
		request = 'fundingRate'

	result = client.Funding.Funding_get(symbol='XBTUSD', reverse=True, count=1).result()
	
	if (request is 'fundingRate') or (request is 'fundingRateDaily'):
		x = str('{0:.4f}%'.format(result[0][0][request] * 100))
	else:
		x = result[0][0][request]
	
	return x


def main():
	client = bitmex.bitmex(test=False, api_key=get_auth('APIKEY'), api_secret=get_auth('SECRET'))

	print('The funding rate is: {}.'.format(get_funding(client)))
	print('The predicted funding rate is: {}.'.format(get_funding(client, request='fundingRateDaily')))
	print('----------\n')
	
if __name__ == "__main__":
	main()
