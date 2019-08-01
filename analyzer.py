#!/usr/bin/env python3

from mapper import Database
from trader import Trader
import datetime

t = datetime.datetime.now()
tm = '{}{}'.format(t.hour,t.minute)

tvix_sl = 0
svxy_sl = 0

def tracker(quotes):
    tvix_change = quotes['tvix_net_change']
    svxy_change = quotes['svxy_net_change']

    if tvix_change > 0.3 and svxy_change < 0.3:
        if tvix_change <= -0.5:
            # TODO: sell function
            pass
        else:
            return Trades.tvix_risk_mgt('TVIX', quotes['tvix_open'], quotes['tvix_current'])
    elif tvix_change < 0.3 and svxy_change > 0.3:
        if svxy_change <= -0.5:
            #sell function
            pass
        else:
            return Trades.svxy_risk_mgt('SVXY', quotes['svxy_open'], quotes['svxy_current'])
    else:
        print('no dice')
