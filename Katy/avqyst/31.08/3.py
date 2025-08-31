from apscheduler.schedulers.background import BackgroundScheduler

import time

def sey():
    print("Работа в фоне")

scheduler = BackgroundScheduler()
scheduler.add_job(sey, "interval", seconds = 2)
scheduler.start()

time.sleep(10)