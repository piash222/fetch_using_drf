from apscheduler.schedulers.background import BackgroundScheduler
from .scheduler import schedule_api

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(schedule_api, 'interval', seconds=900)
	scheduler.start()
