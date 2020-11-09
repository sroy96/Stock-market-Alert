from interfaces.interface import Publisher, stock_list
from utils.notifier import NotificationUtils
from service.loader import LoadStock


class WatchTower(Publisher):
    state = 0
    observser_list = list()

    def attach_observer(self):
        self.observser_list.append(NotificationUtils)

    def detach_observer(self):
        pass

    def notify(self, user_email: str, messages: list):
        print(f"=== user_email is {user_email} ")
        for observers in self.observser_list:
            if observers == NotificationUtils:
                NotificationUtils(user_email=user_email, custom_message=messages).send_mail()

    def business_logic(self, stocks):
        print("===inside business logic ===")
        for stocks_ in stock_list:
            message = []
            stock = stocks_
            stock_nse_code = stock["nse_code"]
            stock_exchange_name = stock["stock_exchange_name"]
            initial_price = stock["price_record"]
            percentage_change = ["set_percentage_margin"]
            stop_loss = stock["stop_loss"]
            target = stock["target"]
            user_email = ["user_email"]
            current_data = LoadStock(nse_code=stock_nse_code, stock_exchange_name=stock_exchange_name).get_all_data()
            if int(current_data["price_current"]) >= int(target):
                self.state = 1
                text = "Hey! " + stock_nse_code + " has reached the target***"
                message.append(text)
            if int(current_data["price_current"]) <= int(stop_loss):
                self.state = 1
                text = "Loosing! " + stock_nse_code + " has gone down "
                message.append(text)
            if int(current_data["price_percent_change"]) >= int(percentage_change):
                self.state = 1
                text = "Hola! " + stock_nse_code + " has reached the set margin percent"
                message.append(text)

            if self.state == 1:
                self.notify(user_email=user_email, messages=message)
            else:
                print(f"=== ALL GOOD NOTHING TO NOTIFY ===")
