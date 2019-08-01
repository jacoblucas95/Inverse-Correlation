#!/usr/bin/env python3

def tracker(quotes):
    time_open = min(quotes, key=int)
    time_now = max(quotes, key=int)
    open_price = quotes[time_open]
    current_price = quotes[time_now]
    tvix_change = current_price['tvix'] - open_price['tvix']
    svxy_change = current_price['svxy'] - open_price['svxy']
    trading_ticker = ''

    if tvix_change > 0.3 and svxy_change < 0.3:
        trading_ticker += 'tvix'
        return tvix_risk_mgt(trading_ticker, open_price, current_price)
    elif tvix_change < 0.3 and svxy_change > 0.3:
        trading_ticker += 'svxy'
        return svxy_risk_mgt(trading_ticker, open_price, current_price)
    else:
        print('no dice')

def tvix_risk_mgt(trading_ticker,open_price, current_price):
    print('tvix')

def svxy_risk_mgt(trading_ticker, open_price, current_price):
    print('svxy')
