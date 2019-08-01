#!/usr/bin/env python3

import json, requests
import time
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from buy_sell_log import log
from analyzer import Trades

API_KEY = 'JRLUCAS'
API_URL = 'https://api.tdameritrade.com/v1/marketdata/quotes'

REFRESH_INTERVAL = 600

scheduler = BackgroundScheduler()
scheduler.start()

def quote_lookup():
    quote_dict = {}
    params = {
        'apikey': API_KEY,
        'symbol': ['TVIX', 'SVXY']
    }

    content = requests.get(url=(API_URL),params=params).text

    data = json.loads(content)

    tvix_open = data['TVIX']['openPrice']
    svxy_open = data['SVXY']['openPrice']

    quote_dict['tvix_open'] = tvix_open
    quote_dict['svxy_open'] = svxy_open

    tvix_current = data['TVIX']['lastPrice']
    svxy_current = data['SVXY']['lastPrice']

    quote_dict['tvix_current'] = tvix_current
    quote_dict['svxy_current'] = svxy_current

    return quote_dict

def main():
    loader()
    scheduler.add_job(loader, 'interval', seconds = REFRESH_INTERVAL)
    while True:
        time.sleep(10)

def loader():
    q = quote_lookup()
    t = datetime.datetime.now()
    current_time = '{}{}'.format(t.hour,t.minute)
    return Trades.tracker(q)


if __name__ == '__main__':
    main()
