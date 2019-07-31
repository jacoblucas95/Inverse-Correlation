#!/usr/bin/env python3

import json, requests

API_KEY = 'JRLUCAS'
API_URL = 'https://api.tdameritrade.com/v1/marketdata/quotes'

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
