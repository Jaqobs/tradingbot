from exchange import ExchData
import tradelogic
import indicators
import time
import logging
import sys
import os
from datetime import datetime
import ordermanager as bitmex


def main():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    logging.basicConfig( 
        level = logging.INFO,
        format = '%(asctime)s  %(levelname)-10s %(processName)s  %(name)s %(message)s',
        handlers=[
            logging.FileHandler('{1}.log'.format(sys.path[0], 
                                time.strftime("tradebot-%Y-%m-%d"))),
            logging.StreamHandler()
            ]
        )
    logging.info('Tradebot started.')
    logging.info('Current path: {}'.format(os.getcwd()))

    #bfx = ExchData('BTC/USDT')
    bmex = ExchData('BTC/USD')
    exch = bmex
    sleep_timer = 60 #3600sec = 1h

    while True:
        exch.clear_candles()
        exch.fetch_candles_long(timeframe='1h', start=52, limit=624)
        candles = exch.get_candles()
        converted_candles = exch.convert_candles(candles, 4)

        candle_open = []
        candle_close = []
        volume = []
        for candle in converted_candles:
            candle_open.append(candle['open'])
            candle_close.append(candle['close'])
            volume.append(candle['volume'])
        
        if (tradelogic.long_open(candle_open, candle_close) and 
            bitmex.has_long_position('BTC/USD') == False):
            bitmex.create_order('BTC/USD', 'market', 'buy', 1)

        if (tradelogic.long_close(candle_open, candle_close) and 
            bitmex.has_long_position('BTC/USD') == True):
            bitmex.close_position('BTC/USD')

        if (tradelogic.short_open(candle_open, candle_close) and 
            bitmex.has_short_position('BTC/USD') == False):
            bitmex.create_order('BTC/USD', 'market', 'sell', 1)

        if (tradelogic.short_close(candle_open, candle_close) and 
            bitmex.has_short_position('BTC/USD') == True):
            bitmex.close_position('BTC/USD')

        lastPrice = bitmex.get_last_price('BTC/USD')
        logging.info('Waiting for next cycle...')
        logging.info('-------------')
        time.sleep(sleep_timer * 5)
    
if __name__ == '__main__':
    main()
