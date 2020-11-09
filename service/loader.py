import requests
from utils import common_constants
from utils.stock_enum import Code
import json
import pprint


class LoadStock(object):
    def __init__(self, nse_code, stock_exchange_name):
        self.nse_code = nse_code
        self.stock_code = Code().stock_code_scrap(nse_code)
        self.stock_exchange_name = stock_exchange_name
        try:
            if stock_exchange_name.lower() == "nse":
                base_url = common_constants.base_url_nse
            elif stock_exchange_name.lower() == "bse":
                base_url = common_constants.base_url_bse
            decoded_data = requests.get(base_url + str(self.stock_code)).content.decode('utf-8')
            self.stock_details = json.loads(decoded_data)
        except ConnectionError:
            print(f"Error creating Connection with Source")
            pass

    def get_dispid(self):
        return self.stock_details['data']['DISPID'],

    def get_current_price(self):
        return self.stock_details['data']['pricecurrent']

    def get_price_change(self):
        return self.stock_details["data"]["pricechange"]

    def get_price_percentage_change(self):
        return self.stock_details["data"]["pricepercentchange"]

    def get_all_data(self):
        return {
                "DISPID": self.get_dispid(),
                "price_current": self.get_current_price(),
                "price_change": self.get_price_change(),
                "price_percent_change": self.get_price_percentage_change()
        }
