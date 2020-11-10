from crontab import CronTab
import sys

sys.path.append('/home/saurav/Documents/Personal_projects/market-notification/service')
cron = CronTab(tabfile='filename.tab')
job = cron.new(
    command='/home/saurav/Documents/Personal_projects/market-notification/venv/bin/python jobber.py ')
job.minute.every(1)

cron.write()
