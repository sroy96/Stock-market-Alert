from enum import Enum
from abc import abstractmethod
from queue import Queue

stock_list = list()


class Resource(Enum):
    pass


class StockToObserve(object):
    def __init__(self, user_email, stock_exchange_name, nse_code, target, stop_loss, set_percent_margin):
        self.user_email = user_email
        self.stock_exchange_name = stock_exchange_name
        self.nse_code = nse_code
        self.target = target
        self.stop_loss = stop_loss
        self.set_percent_margin = set_percent_margin

    def serialize(self):
        serialized_output = {
            "user_email": self.user_email,
            "stock_exchange_name": self.stock_exchange_name,
            "nse_code": self.nse_code,
            "target": self.target,
            "stop_loss": self.stop_loss,
            "set_percentage_margin": self.set_percent_margin
        }
        return serialized_output


class StockUserRelation(StockToObserve):
    @abstractmethod
    def load_current_details(self):
        pass

    @abstractmethod
    def map_stock(self):
        pass

    @abstractmethod
    def add_to_observer_queue(self):
        pass


"""
Our Subject to attach and detach the observer
"""


class Publisher:
    """
    This is the Publisher which notify its Subscribers when stock price change
    """

    @abstractmethod
    def attach_observer(self):
        pass

    @abstractmethod
    def detach_observer(self):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def business_logic(self, stocks):
        pass


class SendEmail(object):
    """
    This is our Observer/subscriber which send the notification to the customer
    when it is notified about any change
    """

    def __init__(self, user_email, custom_message):
        self.custom_message = custom_message
        self.user_email = user_email

    # @abstractmethod
    # def create_smtp_session(self):
    #     pass

    @abstractmethod
    def send_mail(self):
        pass
