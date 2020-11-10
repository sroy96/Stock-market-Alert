from service.watch_tower import WatchTower
from utils import cache_util
from datetime import datetime
import pprint

date_time = datetime.now()
myFile = open('append.txt', 'a')
myFile.write('\nAccessed on ' + str(datetime.now()))
stock_list = cache_util.create_cache_client().get("stock_list")
print(f"=== === === CRON JOB RUNNING At {date_time} === === === with load:-")
for _stocks in stock_list:
    pprint.pprint(_stocks, indent=4)
watch_tower_obj = WatchTower(stock_list)
# watch_tower_obj.attach_observer()
watch_tower_obj.business_logic()
