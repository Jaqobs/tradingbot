#tradelogic by Jaqobs
#4h strategy

import logging

from exchange import ExchData
import indicators as ind
import ordermanager as bitmex



def tradelogic(exchange):

    exchange.clear_candles()
    exchange.fetch_candles(timeframe='5m', start=1, limit=288)
    candles = exchange.get_candles()

    candle_open = []
    candle_high = []
    candle_low = []
    candle_close = []
    volume = []

    for candle in candles:
        candle_open.append(candle['open'])
        candle_close.append(candle['close'])
        volume.append(candle['volume'])

    logging.debug(candle_close)
    logging.debug('-----')
    logging.debug(volume)

    if (long_open(candle_close, volume) and 
            bitmex.has_long_position('BTC/USD') == False):
        bitmex.create_order('BTC/USD', 'market', 'buy', 1)

    if (long_close(candle_close, volume) and 
            bitmex.has_long_position('BTC/USD') == True):
        bitmex.close_position('BTC/USD')

    if (short_open(candle_close, volume) and 
            bitmex.has_short_position('BTC/USD') == False):
        bitmex.create_order('BTC/USD', 'market', 'sell', 1)

    if (short_close(candle_close, volume) and 
            bitmex.has_short_position('BTC/USD') == True):
        bitmex.close_position('BTC/USD')


def long_open(candle_close, volume):
    boolean = False
    current_price = candle_close[0]
    vwma = ind.vwma(candle_close, volume, 200) * 0.913294

    logging.info('Current price: {0:.2f} – Long entry: {1:.2f}'.format(
        current_price, vwma))

    if (current_price < vwma):
        boolean = True    

    return boolean


def long_close(candle_close, volume):
    boolean = False
    current_price = candle_close[0]
    vwma = ind.vwma(candle_close, volume, 200) * 1.015117

    logging.info('Current price: {0:.2f} – Long exit: {1:.2f}'.format(
        current_price, vwma))

    if (current_price > vwma):
        boolean = True    

    return boolean


def short_open(candle_close, volume):
    boolean = False
    current_price = candle_close[0]
    vwma = ind.vwma(candle_close, volume, 200) * 1.036117

    logging.info('Current price: {0:.2f} – Short entry: {1:.2f}'.format(
        current_price, vwma))

    if (current_price > vwma):
        boolean = True    

    return boolean


def short_close(candle_close, volume):
    boolean = False
    current_price = candle_close[0]
    vwma = ind.vwma(candle_close, volume, 200) * 0.985294

    logging.info('Current price: {0:.2f} – Short exit: {1:.2f}'.format(
        current_price, vwma))

    if (current_price < vwma):
        boolean = True    

    return boolean