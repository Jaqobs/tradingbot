#tradelogic by Jaqobs
#4h strategy

import logging

from exchange import ExchData
import indicators as ind
import ordermanager as bitmex



def tradelogic(exchange):

    exchange.clear_candles()
    exchange.fetch_candles_long(timeframe='1h', start=52, limit=624)
    candles = exchange.get_candles()
    converted_candles = exchange.convert_candles(candles, 4)

    candle_open = []
    candle_high = []
    candle_low = []
    candle_close = []
    volume = []

    for candle in converted_candles:
        candle_open.append(candle['open'])
        candle_close.append(candle['close'])
        volume.append(candle['volume'])


    if (long_open(candle_open, candle_close) and 
            bitmex.has_long_position('BTC/USD') == False):
        bitmex.create_order('BTC/USD', 'market', 'buy', 1)

    if (long_close(candle_open, candle_close) and 
            bitmex.has_long_position('BTC/USD') == True):
        bitmex.close_position('BTC/USD')

    if (short_open(candle_open, candle_close) and 
            bitmex.has_short_position('BTC/USD') == False):
        bitmex.create_order('BTC/USD', 'market', 'sell', 1)

    if (short_close(candle_open, candle_close) and 
            bitmex.has_short_position('BTC/USD') == True):
        bitmex.close_position('BTC/USD')


def long_open(data_open, data_close):
    current_price = 0.0
    alma_close = ind.alma(data_close, 300)
    ema_close = ind.ema(data_close, 9)
    ema_open = ind.ema(data_open, 9)
    boolean = False

    logging.info('9Ema Close: {} - 9Ema Open: {} - 300Alma: {}'.format(ema_close, ema_open, alma_close))

    if (ema_close > alma_close) and (ema_open < alma_close):
        boolean = True    
    
    logging.info('Long open: {}'. format(boolean))

    return boolean


def long_close(data_open, data_close):
    current_price = 0.0
    ema_thirty_close = ind.ema(data_close, 30)
    ema_close = ind.ema(data_close, 9)
    ema_open = ind.ema(data_open, 9)
    boolean = False

    logging.info('9Ema: {} - 30Ema: {}'.format(ema_close, ema_thirty_close))

    if (ema_close < ema_thirty_close) and (ema_open > ema_thirty_close):
        boolean = True

    logging.info('Long close: {}'. format(boolean))

    return boolean


def short_open(data_open, data_close):
    current_price = 0.0
    alma_close = ind.alma(data_close, 300)
    ema_close = ind.ema(data_close, 9)
    ema_open = ind.ema(data_open, 9)
    boolean = False

    logging.info('9Ema Close: {} - 9Ema Open: {} - 300Alma: {}'.format(ema_close, ema_open, alma_close))

    if (ema_close < alma_close) and (ema_open > alma_close):
        boolean = True
    
    logging.info('Short open: {}'. format(boolean))
    
    return boolean


def short_close(data_open, data_close):
    current_price = 0.0
    ema_thirty_close = ind.ema(data_close, 30)
    ema_close = ind.ema(data_close, 9)
    ema_open = ind.ema(data_open, 9)
    boolean = False

    logging.info('9Ema: {} - 30Ema: {}'.format(ema_close, ema_thirty_close))

    if (ema_close > ema_thirty_close) and (ema_open < ema_thirty_close):
        boolean = True
        
    logging.info('Short close: {}'. format(boolean))
    
    return boolean