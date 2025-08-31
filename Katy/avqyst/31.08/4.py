from apscheduler.schedulers.background import BackgroundScheduler
import time
from datetime import datetime, timedelta

def sey():
    print("Работа в фоне")

scheduler = BackgroundScheduler()
scheduler.add_job(sey, "date", run_date = datetime.now() + timedelta(seconds=5))
scheduler.start()

while True:
    pass