import configparser
import ccxt
import time
import indicators
from exchange import ExchData
import ordermanager as bitmex
import logging

print(bitmex.has_short_position('BTC/USD'))
print('---')
if (bitmex.has_short_position('BTC/USD')):
	order = bitmex.close_position('BTC/USD')
	print(order)