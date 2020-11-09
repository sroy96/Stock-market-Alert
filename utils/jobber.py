from service.watch_tower import WatchTower
from utils import cache_util
import datetime
import pprint

date_time = datetime.datetime.now()
stock_list = cache_util.create_cache_client().get("stock_list")
print(f"=== === === CRON JOB RUNNING At {date_time} === === === with load:-")
for _stocks in stock_list:
    pprint.pprint(_stocks, indent=4)

watch_tower_obj = WatchTower()
watch_tower_obj.attach_observer()
watch_tower_obj.business_logic(stocks=stock_list)
