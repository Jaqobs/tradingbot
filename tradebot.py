#tradebot framework
#@author: Jaqobs
#@email: jaqobs@jaqobstran.com

import time
import logging
import sys
import os
from datetime import datetime

from exchange import ExchData
import tradelogic



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
        
        #parse candles to the tradelogic
        tradelogic.tradelogic(converted_candles)

        lastPrice = bitmex.get_last_price('BTC/USD')
        logging.info('Waiting for the next cycle...')
        logging.info('-------------')
        time.sleep(sleep_timer * 5)
    
if __name__ == '__main__':
    main()
