#!/usr/bin/env python3

import time
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from loader import quote_lookup
from buy_sell_log import log

REFRESH_INTERVAL = 30

scheduler = BackgroundScheduler()
scheduler.start()
q_dict = {}

def main():
    my_function()
    scheduler.add_job(my_function, 'interval', seconds = REFRESH_INTERVAL)
    while True:
        time.sleep(0.5)

def my_function():
    q = quote_lookup()
    t = datetime.datetime.now()
    current_time = '{}:{}'.format(t.hour,t.minute)
    q_dict[current_time] = q
    print(q_dict)

if __name__ == '__main__':
    main()
