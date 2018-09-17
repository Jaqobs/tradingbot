import ccxt
import datetime

ex = ccxt.bitfinex2({
		'rateLimit': 10000,
		'enableRateLimit': True
		})

#time = ex.iso8601(ex.milliseconds())
time = ex.milliseconds()
print(time)

d = datetime.datetime.utcfromtimestamp(time / 1000).strftime('%H')

print(d)

print(int(d))


