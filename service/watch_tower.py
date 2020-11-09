from interfaces.interface import Publisher, stock_list
from utils.notifier import NotificationUtils
from service.loader import LoadStock
import time

class WatchTower(Publisher):
    state = 0
    observser_list = list()

    def __init__(self, stock_val):
        self.stock_val = stock_val

    def attach_observer(self):
        """
        Implement Observer pattern in future when the observers increase
        :return:
        """
        self.observser_list.append(NotificationUtils.__name__)

    def detach_observer(self):
        pass

    def notify(self, user_email, messages):
        NotificationUtils(user_email=user_email, custom_message=messages).send_mail()

    def business_logic(self):
        for stocks_ in self.stock_val:
            message = []
            stock = stocks_
            stock_nse_code = stock["nse_code"]
            stock_exchange_name = stock["stock_exchange_name"]
            initial_price = stock["price_record"]
            percentage_change = stock["set_percentage_margin"]
            stop_loss = stock["stop_loss"]
            target = stock["target"]
            user_email = stock["user_email"]
            current_data = LoadStock(nse_code=stock_nse_code, stock_exchange_name=stock_exchange_name).get_all_data()
            if float(current_data["price_current"]) >= float(target):
                self.state = 1
                text = "Hey! " + stock_nse_code + " has reached the target***"
                message.append(text)
            if float(current_data["price_current"]) <= float(stop_loss):
                self.state = 1
                text = "Loosing! " + stock_nse_code + " has gone down "
                message.append(text)
            print(type(percentage_change))
            if float(current_data["price_percent_change"]) >= float(percentage_change):
                self.state = 1
                text = "Hola! " + stock_nse_code + " has reached the set margin percent"
                message.append(text)

            if self.state == 1:
                self.notify(user_email=user_email, messages=message)
            else:
                print(f"=== ALL GOOD NOTHING TO NOTIFY ===")
                self.notify(user_email, ["bull run", "sensex boom"])
