#!/usr/bin/env python3

import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler
from loader import loader

REFRESH_INTERVAL = 300

scheduler = BackgroundScheduler()
scheduler.start()

current_time = datetime.datetime.now()

def market_hours():
    if current_time.hour > 10 and current_time.hour < 16:
        return main()
    elif current_time.hour == 9 and current_time.minute >= 30:
        return main()
    else:
        print('not in market hours')

def main():
    pass
    loader()
    scheduler.add_job(loader, 'interval', seconds = REFRESH_INTERVAL)
    while True:
        time.sleep(5)

if __name__ == '__main__':
    market_hours()
    # main()
