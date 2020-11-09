from abc import ABC
from interfaces.interface import StockUserRelation, stock_list
from service import loader
from utils import cache_util
import copy


class UserStocksRelation(StockUserRelation, ABC):
    def load_current_details(self):
        load_object = loader.LoadStock(self.nse_code, self.stock_exchange_name)
        current_details = load_object.get_all_data()
        return current_details

    def map_stock(self):
        stock_dictionary = self.serialize()
        load_state_details = self.load_current_details()
        stock_dictionary["current_details"] = load_state_details
        stock_dictionary["price_record"] = load_state_details["price_current"]
        return stock_dictionary

    def add_to_observer_queue(self):
        stock_list.append(self.map_stock())
        stock_list_copy = stock_list
        cache_util.create_cache_client().delete(key="stock_list")
        # li = [
        #     {"d": "kamal", "s": "were"}]
        cache_util.create_cache_client().set(key="stock_list", value=stock_list_copy)
