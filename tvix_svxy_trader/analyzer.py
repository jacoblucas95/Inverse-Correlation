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
            no_trades = 0

        with Database() as db:
            db.cursor.execute('''SELECT stop_loss FROM log WHERE ticker="{}";
            '''.format('TVIX'))
        try:
            current_stop_loss = db.cursor.fetchall()[-1][0]
        except:
            current_stop_loss = 0

        if current_stop_loss >= quotes['tvix_current']:
            sell_price = quotes['tvix_current']
            print('sold tvix')
            return Trader.tvix_sell_gains(sell_price)

        elif latest_change >= 0.8:
            stop_loss = quotes['svxy_current'] - 0.50
            print('levered tvix')
            return Trader.tvix_buy_trade_log('TVIX',0,
            quotes['tvix_current'],stop_loss)

        elif no_trades == 0:
            stop_loss = quotes['tvix_current'] - 0.50
            print('initial tvix trade')
            return Trader.tvix_buy_trade_log('TVIX',0,
            quotes['tvix_current'],stop_loss)
        else:
            print('no tvix movement')

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

        with Database() as db:
            db.cursor.execute('''SELECT stop_loss FROM log WHERE ticker="{}";
            '''.format('SVXY'))
        try:
            current_stop_loss = db.cursor.fetchall()[-1][0]
        except:
            current_stop_loss = 0

        if current_stop_loss >= quotes['svxy_current']:
            print('sold svxy')
            sell_price = quotes['svxy_current']
            return trader.svxy_sell_gains(sell_price)

        elif latest_change >= 0.8:
            print('levered svxy')
            stop_loss = quotes['svxy_current'] - 0.50
            return Trader.svxy_buy_trade_log('SVXY',0,
            quotes['svxy_current'],stop_loss)

        elif no_trades == 0:
            stop_loss = quotes['svxy_current'] - 0.50
            print('initial svxy trade')
            return Trader.svxy_buy_trade_log('SVXY',0,
            quotes['svxy_current'],stop_loss)
        else:
            print('no svxy movement')
    else:
        print('no dice')
