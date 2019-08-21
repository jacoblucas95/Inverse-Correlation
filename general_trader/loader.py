#!/usr/bin/env python3

import json, requests
import time
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from general_trader import analyzer

API_KEY = 'JRLUCAS'
API_URL = 'https://api.tdameritrade.com/v1/marketdata/quotes'

REFRESH_INTERVAL = 300

scheduler = BackgroundScheduler()
scheduler.start()

def quote_lookup(ticker1,ticker2):
    quote_dict = {}
    params = {
        'apikey': API_KEY,
        'symbol': [ticker1, ticker2]
    }

    content = requests.get(url=(API_URL),params=params).text

    data = json.loads(content)

    t1 = ticker1.lower()
    t2 = ticker2.lower()

    quote_dict['ticker1'] = t1
    quote_dict['ticker2'] = t2

    quote_dict['{}_current'.format(t1)] = data[ticker1]['lastPrice']
    quote_dict['{}_current'.format(t2)] = data[ticker2]['lastPrice']

    quote_dict['{}_net_change'.format(t1)] = data[ticker1]['netChange']
    quote_dict['{}_net_change'.format(t2)] = data[ticker2]['netChange']

    return quote_dict

def main():
    loader()
    scheduler.add_job(loader, 'interval', seconds = REFRESH_INTERVAL)
    while True:
        time.sleep(5)

def loader(ticker1,ticker2):
    q = quote_lookup(ticker1,ticker2)
    print(q)
    return analyzer.tracker(q)

if __name__ == '__main__':
    main()
