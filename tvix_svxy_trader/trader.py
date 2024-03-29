#!/usr/bin/env python3

from mapper import Database
import datetime

t = datetime.datetime.now()
tm = '{}{}'.format(t.hour,t.minute)
dt = '{}{}{}'.format(t.day, t.month, t.year)
date = int(dt)

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
        print('bought tvix')

    def svxy_buy_trade_log(ticker, open_price, current_price, stop_loss):
        with Database() as db:
            db.cursor.execute(
                '''
                    INSERT INTO log(time,ticker,price,stop_loss,volume,buy_sell)
                    VALUES(?,?,?,?,?,?);
                ''',
                    (tm,ticker,current_price,stop_loss,100,'buy')
            )
        print('bought svxy')

    def tvix_sell_gains(sell_price):
        with Database() as db:
            db.cursor.execute(
            '''SELECT * FROM log WHERE ticker="TVIX";'''
            )
            all_trades = db.cursor.fetchall()

        gain_dict = {}
        overall_gains = 0
        for i in all_trades:
            gain = sell_price - i[3]
            gain_dict[i[1]] = gain
        print('closed tvix position')
        gains = 0
        for k,v in gain_dict.items():
            share_gain = v * 100
            gains += share_gain
        print(gains)

        with Database() as db:
            db.cursor.execute(
            '''DELETE FROM log WHERE ticker="TVIX";'''
            )

            db.cursor.execute(
            '''INSERT INTO profit_loss(date, ticker, p_l)
                VALUES(?,?,?);
            ''',(date,'TVIX',gains)
            )

    def svxy_sell_gains(sell_price):
        with Database() as db:
            db.cursor.execute(
            '''SELECT * FROM log WHERE ticker="SVXY";'''
            )
            all_trades = db.cursor.fetchall()

        gain_dict = {}
        overall_gains = 0
        for i in all_trades:
            gain = sell_price - i[3]
            gain_dict[i[1]] = gain
        print('closed svxy position')
        gains = 0
        for k,v in gain_dict.items():
            share_gain = v * 100
            gains += share_gain
        print(gains)

        with Database() as db:
            db.cursor.execute(
            '''DELETE FROM log WHERE ticker="SVXY";'''
            )

            db.cursor.execute(
            '''INSERT INTO profit_loss(date, ticker, p_l)
                VALUES(?,?,?);
            ''',(date,'SVXY',gains)
            )
