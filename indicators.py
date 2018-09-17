#indicators by Jaqobs
import math

#Arnaud Legoux Moving Average
def alma(data, length, offset=None, sigma=None):
	series = data[0:length]

	if offset == None:
		offset = 0.85

	if sigma == None:
		sigma = 6.0

	m = math.floor(offset * (length - 1))
	s = float(length) / sigma
	norm = 0.0
	sums = 0.0

	for i in range(length):
		weight = math.exp(-1 * math.pow(i - m, 2) / (2 * math.pow(s, 2)))
		norm += weight
		sums += series[length - i - 1] * weight

	print('Alma {}: {}'.format(length, (sums / norm)))	#debugging
	return sums / norm


#Moving Average
def sma(data, length):
	series = data[0:length]
	x = 0.0		#sum of price
	for i in series:
		x += i

	print('SMA {}: {}'.format(length, (x / length)))	#debugging
	return x / length

#Exponential Moving Average
def ema(data, length):
	series = data
	m = 2.0 / (length + 1)		#weighted multiplier
	x = series[len(series)-1]	#seed value

	for i in reversed(series):
		if i is not x:
			x = i * m + x * (1.0 - m)
		
	print('EMA {}: {}'.format(length, x))	#debugging
	return x

#Volume Weighted Moving Average
def vwma(data, volume, length):
	price_series = data[0:length]
	vol_series = volume[0:length]
	x = 0.0		#price * volume
	y = 0.0		#sum of volume
	
	for count in range(len(price_series)):
		x += price_series[count] * vol_series[count]

	for vol in vol_series:
		y += vol

	print('VWMA {}: {}'.format(length, (x / y)))	#debugging
	return x / y
	