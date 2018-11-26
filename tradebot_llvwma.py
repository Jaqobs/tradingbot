#tradebot framework
#@author: Jaqobs
#@email: jaqobs@jaqobstran.com

import time
import logging
import sys
import os
from datetime import datetime

from exchange import ExchData
import tradelogicllvwma
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
    logging.info('Strategy: LLVWMA Scalping')
    logging.info('Current path: {}'.format(os.getcwd()))

    #bfx = ExchData('BTC/USDT')
    bmex = ExchData('BTC/USD')
    exch = bmex
    sleep_timer = 60 #3600sec = 1h

    while True:
        #parse exchange to the tradelogic
        tradelogicllvwma.tradelogic(exch)

        lastPrice = bitmex.get_last_price('BTC/USD')
        logging.info('Waiting for the next cycle...')
        logging.info('-------------')
        time.sleep(sleep_timer * 5)
    
if __name__ == '__main__':
    main()
