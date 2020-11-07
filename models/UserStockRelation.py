from abc import ABC
import pprint
from interfaces.interface import StockUserRelation, stock_list
from service import loader


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
        stock_list.put(self.map_stock())
        while stock_list:
            pprint.pprint(stock_list.get(), indent=4)
            stock_list.task_done()
