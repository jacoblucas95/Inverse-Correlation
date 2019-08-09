#!/usr/bin/env python3

from mapper import Database
import datetime

t = datetime.datetime.now()
tm = '{}{}'.format(t.hour,t.minute)

class Trader:
    def __init__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self):
        pass

    def tvix_buy_trade_log(ticker, open_price, current_price, stop_loss):
        with Database() as db:
            db.cursor.execute(
                '''
                    INSERT INTO log(time,ticker,price,stop_loss,volume,buy_sell)
                    VALUES(?,?,?,?,?,?);
                ''',
                    (tm,ticker,current_price,stop_loss,100,'buy')
            )
        print('bought')

    def svxy_buy_trade_log(ticker, open_price, current_price, stop_loss):
        with Database() as db:
            db.cursor.execute(
                '''
                    INSERT INTO log(time,ticker,price,stop_loss,volume,buy_sell)
                    VALUES(?,?,?,?,?,?);
                ''',
                    (tm,ticker,current_price,stop_loss,100,'buy')
            )
        print('bought')

    def tvix_sell_gains(sell_price):
        pass

    def svxy_sell_gains(sell_price):
        with Database() as db:
            db.cursor.execute(
            '''SELECT * FROM log WHERE ticker="SVXY";'''
            )
            all_trades = db.cursor.fetchall()

        gain_dict = {}
        overall_gains = 0
        for i in all_trades:
            gain = i[3] - sell_price
            gain_dict[i[1]] = gain

        print(gain_dict)
