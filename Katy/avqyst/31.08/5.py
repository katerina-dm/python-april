from apscheduler.schedulers.background import BackgroundScheduler
import time
from datetime import datetime, timedelta

def sey():
    print("Ежедневная задачи")

scheduler = BackgroundScheduler()
#scheduler.add_job(sey, "cron", hour=19, minute=4)
scheduler.add_job(
    sey, 
    "cron",
    day_of_week ="mon, wen",
    months="1,2",
    hour= "18-18/2",
    minute=0)

scheduler.start()

while True:
    pass