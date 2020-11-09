from service.watch_tower import WatchTower
from interfaces.interface import stock_list
from utils import cache_util
import datetime
import pprint

# date_time = datetime.datetime.now()
# print(f"=== === === CRON JOB RUNNING At {date_time} === === === ")
# watch_tower_obj = WatchTower()
# watch_tower_obj.attach_observer()
# watch_tower_obj.business_logic()
stock_list = cache_util.create_cache_client().get("stock_list")
print(stock_list)