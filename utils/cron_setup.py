from crontab import CronTab

cron = CronTab(tabfile='filename.tab')
job = cron.new(
    command='/home/saurav/Documents/Personal_projects/market-notification/venv/bin/python jobber.py ')
job.minute.every(1)

cron.write()
