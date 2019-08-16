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
            all_trades = db.cursor.fetchall()
        try:
            latest_trade_price = all_trades[-1][0]
            no_trades = len(all_trades)
            latest_change = quotes['tvix_current'] - latest_trade_price
        except:
            latest_trade_price = 0
            latest_change = 0

        if latest_change >= 0.8:
            stop_loss = quotes['svxy_current'] - 0.50
            return Trader.tvix_buy_trade_log('TVIX',0,
            quotes['tvix_current'],stop_loss)

        elif no_trades == 0:
            stop_loss = quotes['tvix_current'] - 0.50
            return Trader.tvix_buy_trade_log('TVIX',0,
            quotes['tvix_current'],stop_loss)
        else:
            sell_price = quotes['tvix_current']
            return Trader.tvix_sell_gains(sell_price)
            print('no tvix trades')

    elif tvix_change < 0.3 and svxy_change > 0.3:
        with Database() as db:
            db.cursor.execute('''SELECT price FROM log WHERE ticker="{}";
            '''.format('SVXY'))
            all_trades = db.cursor.fetchall()
        try:
            latest_trade_price = all_trades[-1][0]
            no_trades = len(all_trades)
            latest_change = quotes['svxy_current'] - latest_trade_price
        except:
            latest_trade_price = 0
            latest_change = 0
            no_trades = 0

        if latest_change >= 0.8:
            # TODO: lever up
            stop_loss = quotes['svxy_current'] - 0.50
            return Trader.svxy_buy_trade_log('SVXY',0,
            quotes['svxy_current'],stop_loss)

        elif no_trades == 0:
            # initial trade at 100 shares
            stop_loss = quotes['svxy_current'] - 0.50
            return Trader.svxy_buy_trade_log('SVXY',0,
            quotes['svxy_current'],stop_loss)
        else:
            print('no trades for svxy')
    else:
        print('no dice')
