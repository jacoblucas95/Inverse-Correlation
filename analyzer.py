#!/usr/bin/env python3

def tracker(quotes):
    time_open = min(quotes, key=int)
    time_now = max(quotes, key=int)
    open_price = quotes[time_open]
    current_price = quotes[time_now]
    tvix_change = current_price['tvix'] - open_price['tvix']
    svxy_change = current_price['svxy'] - open_price['svxy']

    print(tvix_change)
    print(svxy_change)
