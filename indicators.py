#indicators by Jaqobs
import math

#Arnaud Legoux Moving Average
def alma(data, length, offset=None, sigma=None):	#buggy
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
		weight = math.exp(-1 * math.pow(i - m, 2) / 2 * math.pow(s, 2))
		norm += norm + weight
		sums += sums + series[length - i - 1] * weight
		print('Result: ' + str(sums/norm))		#debugging

	return sums / norm

#Moving Average
def sma(data, length):
	series = data[0:length]
	x = 0.0		#sum of price
	for i in series:
		x += i

	return x / length

#Exponential Moving Average
def ema(data, length):
	series = data
	m = 2.0 / (length + 1)		#weighted multiplier
	x = series[len(series)-1]	#seed value

	for i in reversed(series):
		if i is not x:
			x = i * m + x * (1.0 - m)
		
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

	return x / y


#testing
test = [
		1.16174, 1.16006, 1.16709, 1.17068, 1.16940, 
		1.16774, 1.16194, 1.15378, 1.15969, 1.15705, 
		1.14816, 1.14362, 1.13766, 1.13451, 1.13439, 
		1.14097, 1.14111
		]
test_vol = [
		145.485, 355.52, 320.145, 316.929, 
		297.633, 239.747, 310.497, 300.849, 
		307.281, 349.088
		]

print('This is ALMA: ' + str(alma(test, 5)))
	