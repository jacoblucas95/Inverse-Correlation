#!/usr/bin/env python3

import json, requests
import time
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from analyzer import tracker

API_KEY = 'JRLUCAS'
API_URL = 'https://api.tdameritrade.com/v1/marketdata/quotes'

REFRESH_INTERVAL = 300

scheduler = BackgroundScheduler()
scheduler.start()

def quote_lookup(ticker1, ticker2):
    quote_dict = {}
    params = {
        'apikey': API_KEY,
        'symbol': [ticker1, ticker2]
    }

    content = requests.get(url=(API_URL),params=params).text

    data = json.loads(content)

    '{}_current'.format(ticker1) = data[ticker1]['lastPrice']
    '{}_current'.format(ticker1) = data[ticker2]['lastPrice']

    quote_dict['{}_current'].format(ticker1) = tvix_current
    quote_dict['{}_current'].format(ticker2) = svxy_current

    tvix_net_change = data['{}'.format(ticker1)]['regularMarketNetChange']
    svxy_net_change = data['{}'.format(ticker2)]['regularMarketNetChange']

    # quote_dict['tvix_net_change'] = tvix_net_change
    # quote_dict['svxy_net_change'] = svxy_net_change
    print(quote_dict)
    return quote_dict

def main():
    loader()
    scheduler.add_job(loader, 'interval', seconds = REFRESH_INTERVAL)
    while True:
        time.sleep(5)

def loader():
    q = quote_lookup()
    return q
    t = datetime.datetime.now()
    current_time = '{}{}'.format(t.hour,t.minute)
    return tracker(q)

if __name__ == '__main__':
    main()
