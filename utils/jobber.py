from datetime import datetime
import pprint
from service.watch_tower import WatchTower
from utils import cache_util
import sched, time
from utils import common_constants

scheduler = sched.scheduler(time.time, time.sleep)


def ring_jobber():
    if cache_util.create_cache_client().check_key(common_constants.CACHE_KEY):
        stock_list = cache_util.create_cache_client().get(common_constants.CACHE_KEY)
        if len(stock_list) > 0:
            date_time = datetime.now()
            my_file = open('jobber_logs.txt', 'a')
            my_file.write(f'\n=== === === SCHEDULE JOB RUNNING At {date_time} and load size {len(stock_list)} === === ===')
            for _stocks in stock_list:
                pprint.pprint(_stocks, indent=4)
            watch_tower_obj = WatchTower(stock_list)
            watch_tower_obj.business_logic()
    else:
        pass


while True:
    ring_jobber()
    time.sleep(180)
