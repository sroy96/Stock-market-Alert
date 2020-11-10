from interfaces.interface import Publisher, stock_list
from utils.notifier import NotificationUtils
from service.loader import LoadStock
from utils import cache_util, common_constants


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
        new_stock_list = list()
        for stocks_ in self.stock_val:
            message = []
            stock = stocks_
            stock_nse_code = stock[common_constants.NSE_CODE]
            stock_exchange_name = stock[common_constants.STOCK_EXCHANGE]
            initial_price = stock[common_constants.PRICE_RECORD]
            percentage_change = stock[common_constants.PERCENT_MARGIN]
            stop_loss = stock[common_constants.STOP_LOSS]
            target = stock[common_constants.TARGET]
            user_email = stock[common_constants.USER_EMAIL]
            current_data = LoadStock(nse_code=stock_nse_code, stock_exchange_name=stock_exchange_name).get_all_data()
            if float(current_data[common_constants.CURRENT_PRICE]) >= float(target):
                self.state = 1
                text = "Hey! " + stock_nse_code + " has reached the target***"
                message.append(text)
            if float(current_data[common_constants.CURRENT_PRICE]) <= float(stop_loss):
                self.state = 1
                text = "Loosing! " + stock_nse_code + " has gone down "
                message.append(text)
            print(type(percentage_change))
            if float(current_data[common_constants.PRICE_PERCENTAGE_CHANGE]) >= float(percentage_change):
                self.state = 1
                text = "Hola! " + stock_nse_code + " has reached the set margin percent"
                message.append(text)

            if self.state == 1:
                self.notify(user_email=user_email, messages=message)
            else:
                print(f"=== ALL GOOD NOTHING TO NOTIFY ===")
                self.notify(user_email, ["bull run", "sensex boom"])

            stock[common_constants.CURRENT_DETAILS] = current_data
            new_stock_list.append(stock)

        print(type(new_stock_list))
        cache_util.create_cache_client().set(common_constants.CACHE_KEY, new_stock_list)
