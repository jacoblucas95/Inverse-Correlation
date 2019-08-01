#!/usr/bin/env python3

from mapper import Database

class Trader:
    def __init__(self, ticker, signal):
        pass

    def __enter__(self):
        return self

    def __exit__(self):
        pass

    def tvix_trade_log(ticker,open_price, current_price):
        with Database() as db:
            db.cursor.execute(
                '''
                    INSERT INTO log(time,ticker,price,volume,buy_sell)
                    VALUES(?,?,?,?,?);
                ''',
                    (tm,ticker,current_price,'buy')
            )

    def svxy_trade_log(ticker, open_price, current_price):
        with Database() as db:
            db.cursor.execute(
                '''INSERT INTO log(time,ticker,price,volume,buy_sell)
                    VALUES(?,?,?,?,?);
                ''',
                    (tm,ticker,current_price,100,'buy')
            )
        print('bought')
