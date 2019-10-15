#!/usr/bin/env python3

import datetime
import schedule
import time
from apscheduler.schedulers.background import BackgroundScheduler
from loader import Loader

current_time = datetime.datetime.now()
def market_hours():
    if current_time.hour >= 10 and current_time.hour < 16:
        return Loader.loader()
    elif current_time.hour == 9 and current_time.minute >= 30:
        return Loader.loader()
    else:
        print('closed')

schedule.every(5).minutes.do(market_hours)

while True:
    # print('while loop')
    schedule.run_pending()
    time.sleep(5)
