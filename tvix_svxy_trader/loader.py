#!/usr/bin/env python3

import json, requests
from analyzer import tracker
from mapper import Database
from trader import Trader
from config import client_id

API_KEY = client_id
API_URL = 'https://api.tdameritrade.com/v1/marketdata/quotes'

def quote_lookup():
    quote_dict = {}
    params = {
        'apikey': API_KEY,
        'symbol': ['TVIX', 'SVXY']
    }

    content = requests.get(url=(API_URL),params=params).text

    data = json.loads(content)

    tvix_current = data['TVIX']['lastPrice']
    svxy_current = data['SVXY']['lastPrice']

    quote_dict['tvix_current'] = tvix_current
    quote_dict['svxy_current'] = svxy_current

    tvix_net_change = data['TVIX']['netChange']
    svxy_net_change = data['SVXY']['netChange']

    quote_dict['tvix_net_change'] = tvix_net_change
    quote_dict['svxy_net_change'] = svxy_net_change

    return quote_dict

def loader():
    q = quote_lookup()
    print(q)
    with Database() as db:
        db.cursor.execute('''SELECT stop_loss FROM log;''')
        all_stop_loss = db.cursor.fetchall()
    try:
        latest_stop_loss = all_stop_loss[-1][0]
    except:
        pass
    with Database() as db:
        try:
            db.cursor.execute('''SELECT ticker from log WHERE stop_loss="{}";
            '''.format(latest_stop_loss))
            ticker = db.cursor.fetchone()[0]
            tick = ticker.lower()
            tick_current = q['{}_current'.format(tick)]
            if latest_stop_loss >= tick_current:
                if tick == 'tvix':
                    return Trader.tvix_sell_gains(tick_current)
                else:
                    return Trader.svxy_sell_gains(tick_current)
            else:
                return tracker(q)
        except:
            return tracker(q)
