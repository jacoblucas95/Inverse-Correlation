#!/usr/bin/env python3

from general_trader import mapper
from general_trader import trader
import datetime

t = datetime.datetime.now()
tm = '{}{}'.format(t.hour,t.minute)

def tracker(quotes):
    ticker1 = quotes['ticker1']
    ticker2 = quotes['ticker2']
    t1_change = quotes['{}_net_change'.format(ticker1)]
    t2_change = quotes['{}_net_change'.format(ticker2)]

    if t1_change > 0.3 and t2_change < 0.3:
        with mapper.Database() as db:
            db.cursor.execute('''SELECT price FROM log WHERE ticker="{}";
            '''.format(ticker1))
            all_trades = db.cursor.fetchall()
        try:
            latest_trade_price = all_trades[-1][0]
            no_trades = len(all_trades)
            latest_change = quotes['{}_current'.format(ticker1)] - latest_trade_price
        except:
            latest_trade_price = 0
            latest_change = 0
            no_trades = 0

        if latest_change >= 0.8:
            stop_loss = quotes['{}_current'.format(ticker1)] - 0.50
            return Trader.buy_trade_log(ticker1,0,
            quotes['{}_current'.format(ticker1)],stop_loss)

        elif no_trades == 0:
            stop_loss = quotes['{}_current'.format(ticker1)] - 0.50
            return Trader.buy_trade_log(ticker1,0,
            quotes['{}_current'.format(ticker1)],stop_loss)
        else:
            print('no {} trades'.format(ticker1))

    elif t1_change < 0.3 and t2_change > 0.3:
        with mapper.mapper.Database() as db:
            db.cursor.execute('''SELECT price FROM log WHERE ticker="{}";
            '''.format(ticker2))
            all_trades = db.cursor.fetchall()
        try:
            latest_trade_price = all_trades[-1][0]
            no_trades = len(all_trades)
            latest_change = quotes['{}_current'.format(ticker2)] - latest_trade_price
        except:
            latest_trade_price = 0
            latest_change = 0
            no_trades = 0

        if latest_change >= 0.8:
            stop_loss = quotes['{}_current'.format(ticker2)] - 0.50
            return Trader.buy_trade_log(ticker2,0,
            quotes['{}_current'.format(ticker2)],stop_loss)

        elif no_trades == 0:
            stop_loss = quotes['{}_current'.format(ticker2)] - 0.50
            return Trader.buy_trade_log(ticker2,0,
            quotes['{}_current'.format(ticker2)],stop_loss)
        else:
            print('no trades for {}'.format(ticker2))
    else:
        print('no dice')
