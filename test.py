import configparser
import ccxt
import time
import indicators
from exchange import ExchData
import ordermanager as bitmex

print(bitmex.get_all_open_positions())
print('---')
print(bitmex.get_open_position('BTC/USD'))
print('---')
print(bitmex.get_open_position('XBTUSD'))
print('---')
print(bitmex.get_open_position('ETHUSD'))
print('---')
bitmex.close_position('BTC/USD')