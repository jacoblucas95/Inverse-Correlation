#!/usr/bin/env python3

import json, requests
import time
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from buy_sell_log import log
from analyzer import tracker

API_KEY = 'JRLUCAS'
API_URL = 'https://api.tdameritrade.com/v1/marketdata/quotes'

REFRESH_INTERVAL = 30

scheduler = BackgroundScheduler()
scheduler.start()
q_dict = {}

def quote_lookup():
    quote_dict = {}
    params = {
        'apikey': API_KEY,
        'symbol': ['TVIX', 'SVXY']
    }

    content = requests.get(url=(API_URL),params=params).text

    data = json.loads(content)

    tvix = data['TVIX']['lastPrice']
    svxy = data['SVXY']['lastPrice']

    quote_dict['tvix'] = tvix
    quote_dict['svxy'] = svxy

    return quote_dict

def main():
    loader()
    scheduler.add_job(loader, 'interval', seconds = REFRESH_INTERVAL)
    while True:
        time.sleep(0.5)

def loader():
    q = quote_lookup()
    t = datetime.datetime.now()
    current_time = '{}{}'.format(t.hour,t.minute)
    q_dict[current_time] = q
    return tracker(q_dict)


if __name__ == '__main__':
    main()
