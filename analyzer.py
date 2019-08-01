#!/usr/bin/env python3

from mapper import Database
import datetime

t = datetime.datetime.now()
tm = '{}{}'.format(t.hour,t.minute)

class Trades:
    def __init__(self, tvix_sl, svxy_sl):
        self.tvix_sl = 0
        self.svxy_sl = 0

    def tracker(quotes):
        tvix_change = quotes['tvix_current'] - quotes['tvix_open']
        svxy_change = quotes['svxy_current'] - quotes['svxy_open']
        trading_ticker = ''

        if tvix_change > 0.3 and svxy_change < 0.3:
            if tvix_change <= -0.5:
                #sell function
                pass
            else:
                trading_ticker += 'tvix'
                return tvix_risk_mgt(trading_ticker, quotes['tvix_open'], quotes['tvix_current'])
        elif tvix_change < 0.3 and svxy_change > 0.3:
            if svxy_change <= -0.5:
                #sell function
                pass
            else:
                trading_ticker += 'svxy'
                return svxy_risk_mgt(trading_ticker, quotes['svxy_open'], quotes['svxy_current'])
        else:
            print('no dice')

    def tvix_risk_mgt(ticker,open_price, current_price):
        if current_price - open_price >= 0.8:
            #lever up position
            pass
        else:
            pass
            with Database() as db:
                db.cursor.execute(
                    '''
                        INSERT INTO log(time,ticker,price,volume,buy_sell)
                        VALUES(?,?,?,?,?);
                    ''',
                        (tm,ticker,current_price,'buy')
                )

    def svxy_risk_mgt(ticker, open_price, current_price):
        if current_price - open_price >= 0.8:
            self.svxy_sl = current_price
            with Database() as db:
                db.cursor.execute(
                '''SELECT volume FROM log WHERE ticker="{}";
                '''.format(ticker)
                )
            volume = db.cursor.fetchone()[0]
            volume += 100
        else:
            self.svxy_sl = current_price
            with Database() as db:
                db.cursor.execute(
                    '''INSERT INTO log(time,ticker,price,volume,buy_sell)
                        VALUES(?,?,?,?,?);
                    ''',
                        (tm,ticker,current_price,100,'buy')
                )
            print('bought')
