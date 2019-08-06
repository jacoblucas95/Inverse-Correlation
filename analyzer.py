#!/usr/bin/env python3

from mapper import Database
from trader import Trader
import datetime

t = datetime.datetime.now()
tm = '{}{}'.format(t.hour,t.minute)

def tracker(quotes):
    tvix_change = quotes['tvix_net_change']
    svxy_change = quotes['svxy_net_change']

    if tvix_change > 0.3 and svxy_change < 0.3:
        with Database() as db:
            db.cursor.execute('''SELECT price FROM log WHERE ticker="{}";
            '''.format('TVIX'))
            latest_trade_price = db.cursor.fetchall()[-1][0]
        latest_change = quotes['tvix_current'] - latest_trade_price
        if latest_change >= 0.8 or latest_change <= -0.5:
            return Trader.tvix_trade_log('TVIX',quotes['tvix_open'],quotes['tvix_current'])
            # TODO: buy and sell
        else:
            return Trader.tvix_trade_log('TVIX',quotes['tvix_open'],quotes['tvix_current'])
        # if tvix_change <= -0.5:
        #     # TODO: sell function
        #     pass
        # else:
        #     pass
            # return Trades.tvix_risk_mgt('TVIX', quotes['tvix_open'], quotes['tvix_current'])
    elif tvix_change < 0.3 and svxy_change > 0.3:
        svxy_sl += quotes['svxy_current']
        if svxy_change <= -0.5:
            #sell function
            pass
        else:
            pass
            # return Trades.svxy_risk_mgt('SVXY', quotes['svxy_open'], quotes['svxy_current'])
    else:
        print('no dice')
